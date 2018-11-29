__author__ = 'Victor'

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
from nltk import wordpunct_tokenize
import re
from langdetect import detect
import json




spanish_stop = stopwords.words('spanish')
english_stop = stopwords.words('english')
all_stopwords = spanish_stop + english_stop
non_words = list(punctuation)

#we add spanish punctuation
non_words.extend(['¿', '¡'])
non_words.extend(map(str,range(10)))




__replacement_patterns = [(r'[wW]on\'t', 'will not'),
                        (r'[cC]an\'t', 'can not'),
                        (r'[iI]\'m', 'i am'),
                        (r'[aA]in\'t', 'is not'),
                        (r'[iI]t\'s', 'it is'),
                        (r'(\w+)\'ll', '\g<1> will'),
                        (r'(\w+)n\'t', '\g<1> not'),
                        (r'(\w+)\'ve', '\g<1> have'),
                        (r'(\w+)\'s', '\g<1>'),
                        (r'(\w+)\'re', '\g<1> are'),
                        (r'(\w+)\'em', '\g<1> them'),
                        (r'[nN]\'t', 'not'),
                        (r'\'m', 'am'),
                        (r'\'s', 'is'),
                        (r'\'ll', 'will'),
                        (r'\'ve', 'have'),
                        (r'\'re', 'are'),
                        (r'Á', 'A'),
                        (r'É', 'E'),
                        (r'Í', 'I'),
                        (r'Ó', 'O'),
                        (r'Ú', 'U'),
                        (r'ü', 'u'),
                        (r'&', 'and'),
                        (r'%', 'percent')]

def text_work(json_request):
    data = json.loads(json_request)
    if data['action'] == 'process':
        terms = __tokenisation(data['data'])
        return json.dumps({'terms': terms})


def __replace( text):
    s = text
    for (pattern, repl) in __replacement_patterns:
        s = re.sub(pattern, repl, s)
    return s


def __tokenisation(data):

    pattern = r'([a-zA-z]+)'

    match = re.search(pattern, data)

    if len(data)==0 or not match:
        return []

    data = __replace(data)

    lang = detect(data)
    tokens = wordpunct_tokenize(data)

    tokens = [elem for elem in tokens if (elem not in all_stopwords and elem not in non_words)]

    stemmer = SnowballStemmer('spanish') if lang == 'es' else SnowballStemmer('english')

    tokens_stem = [stemmer.stem(token) for token in tokens]

    return tokens_stem
