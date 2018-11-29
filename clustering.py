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
stemmer = SnowballStemmer("english")


titles = []
text = []
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

def clustering(path_to_corpus):
    __load_corpus(path_to_corpus)
    pass

print(stopwords[0:10])