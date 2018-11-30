import json
import index
from text_proc import text_work
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.externals import joblib
from sklearn.cluster import KMeans
stemmer = SnowballStemmer("english")

titles = []
text = []
totalvocab_stemmed = []
totalvocab_tokenized = []
vocab_frame = None
tfidf_vectorizer = None
tfidf_matrix = None
terms = None
dist = None
km = None
cluster = None
frame = None
docs = None
stopwords = nltk.corpus.stopwords.words('english')
doc_clust = {}
clust_docs = {}

def __load_corpus(path):
    # if os.path.isdir('doc_cluster.pkl'):
    #     km = joblib.load('doc_cluster.pkl')
    #     clusters = km.labels_.tolist()
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root,filename), encoding='utf8', errors='ignore') as f:
                    titles.append(filename)
                    text.append(f.read())

def __tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]',token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def __tokenize_and_stem_all():
    for i in text:
        allwords_stemmed = __tokenize_and_stem(i) #for each item in 'text', tokenize/stem
        totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
        allwords_tokenized = __tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)

def __tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

def __tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def __creating_Pandas():
    global vocab_frame
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    print ('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
    print (vocab_frame.head())    

def __tf_idf():
    global tfidf_vectorizer, tfidf_matrix, terms, dist
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.2, stop_words='english',use_idf=True,tokenizer=__tokenize_and_stem,ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(text)
    terms = tfidf_vectorizer.get_feature_names()
    dist = 1 - cosine_similarity(tfidf_matrix)
    print(tfidf_matrix.shape)

def __clustering(num_clusters):
    global km,clusters,frame,docs
    # if not os.path.isdir('doc_cluster.pkl'):
    km = KMeans(n_clusters=num_clusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()
    # joblib.dump(km,'doc_cluster.pkl')
    docs =  {    
            'title' : titles, 
            'text' : text,
            'cluster':cluster
            }
    frame = pd.DataFrame(docs,index=[clusters],columns=['title','cluster'])
    frame['cluster'].value_counts()        

def __printer(num_clusters):
    print("Top terms per cluster:")
    print()
    #sort cluster centers by proximity to centroid
    order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

    for i in range(num_clusters):
        print("Cluster %d words:" % i, end='')
        doc_list = []
        label_list = []
        
        for ind in order_centroids[i, : 3]: 
            print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
            label_list.append(str(vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore')))            
        print() 
        print() 
        
        print("Cluster %d titles:" % i, end='')
        for title in frame.ix[i]['title'].values.tolist():
            print(' %s,' % title, end='')
            doc_list.append(title)
            doc_clust[title] = i
        clust_docs[i] = (doc_list,label_list)
        print() 
        print() 
    print()
    print()

def all_doc_from_cluster(doc_name):
    return clust_docs[doc_clust[doc_name]][0]

def all_label_from_cluster(doc_name):
    return clust_docs[doc_clust[doc_name]][1]

def clustering(path_to_corpus,num_clusters):
    __load_corpus(path_to_corpus)   
    __tokenize_and_stem_all()       
    __creating_Pandas()             
    __tf_idf()
    __clustering(num_clusters)
    __printer(num_clusters)

# clustering('clust_training',5)
# print(all_doc_from_cluster('1.txt'))
# print(all_label_from_cluster('1.txt'))