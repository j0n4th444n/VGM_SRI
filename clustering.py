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
stemmer = SnowballStemmer("english")

titles = []
text = []
totalvocab_stemmed = []
totalvocab_tokenized = []
vocab_frame = None
stopwords = nltk.corpus.stopwords.words('english')

def __load_corpus(path):
    if os.path.isdir(path):
        for filename in os.listdir(path):
            with open(os.path.join(path, filename, encoding='utf8', errors='ignore')) as f:
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
        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

def __creating_Pandas():
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    print ('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
    print (vocab_frame.head())

def clustering(path_to_corpus):
    __load_corpus(path_to_corpus)
    __tokenize_and_stem_all()
    __creating_Pandas()
    pass


print(stopwords[0:10])