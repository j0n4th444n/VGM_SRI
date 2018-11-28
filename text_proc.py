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




replacement_patterns = [(r'[wW]on\'t', 'will not'),
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
        terms = tokenisation(data['data'])
        return json.dumps({'terms': terms})


def replace( text):
    s = text
    for (pattern, repl) in replacement_patterns:
        s = re.sub(pattern, repl, s)
    return s


def tokenisation(data):

    data = replace(data)

    lang = detect(data)
    tokens = wordpunct_tokenize(data)

    tokens = [elem for elem in tokens if (elem not in all_stopwords and elem not in non_words)]

    stemmer = SnowballStemmer('spanish') if lang == 'es' else SnowballStemmer('english')

    tokens_stem = [stemmer.stem(token) for token in tokens]

    return tokens_stem





if __name__ == "__main__":
    text = """  If this book: "has" a central thesis, it rests upon the simple but
frequently neglected principle that college library service goes
beyond the commonly accepted functions of book circulation and
storage.  The college library exists, not merely to house and
circulate library materials, but to supplement and extend the teaching
process with reference service, to afford faculty members library
opportunities for improving instruction, and to encourage students
to read more and better books.  Administration's essentially a
service activity, a tool through which library aren't functions're more
fully and efficiently realized.
  The present work retains most of the material of the first edition,
but includes substantial revision in each chapter.  The book was
planned not only as a text in the teaching of college library
administration but also for independent professional reading.  Because
readers have found the footnotes and chapter bibliographies useful
for reference purposes, they have been brought up to date and in
some cases extended.
"""

    # tokens= text_work(text)
    # tokens = wordpunct_tokenize(text)
    # tokens = word_tokenize(text)

    # tokens = _clean_text(text)
    #
    # for elem in tokens:
    #     print(elem)
    #
    # print("s" in stopwords.words('spanish'))
    # print(stopwords.words('spanish'))
    tokens = tokenisation(text)

    for el in tokens:
        print(el)