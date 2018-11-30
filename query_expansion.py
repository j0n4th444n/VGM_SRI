from nltk.corpus import stopwords
from string import punctuation
from nltk import wordpunct_tokenize
import json
import modelo
import index
from nltk.corpus import wordnet as wn
from langdetect import detect



def start(json_request):

    data = json.loads(json_request)
    json_result = json.loads(modelo.request_query(data['query'], data['count'], data['similarity_techniques']))
    documents = [pair["document"] for pair in json_result['results']]

    relevant_words =  pseudo_Relevance_Feedback(documents)

    words = data['query'] + " " + relevant_words

    if detect(data['query']) == 'en':
        words = words + " " + expansion_synonyms(data['query'])

    return modelo.request_query(words, data['count'], data['similarity_techniques'])


def pseudo_Relevance_Feedback(documents):

    relevant_words = set()

    for doc in documents:
        json_request = json.dumps({'action': 'terms_frec', 'key': doc})
        json_response = json.loads(index.start(json_request))
        lista = json_response['terms']
        lista.sort(key=lambda x: x[1], reverse=True)
        relevant_words.add(lista[0][0])

    return " ".join(list(relevant_words))

def expansion_synonyms(data):

    spanish_stop = stopwords.words('spanish')
    english_stop = stopwords.words('english')
    all_stopwords = spanish_stop + english_stop
    non_words = list(punctuation)

    # we add spanish punctuation
    non_words.extend(['¿', '¡'])
    non_words.extend(map(str, range(10)))
    tokens = wordpunct_tokenize(data)

    tokens = [elem for elem in tokens if (elem not in all_stopwords and elem not in non_words)]

    words=[]
    synonyms = []
    for token in tokens:
        print(token)
        for syn in wn.synsets(token):
            # print(syn.lemmas())
            for lm in syn.lemmas():
                # print(lm/)
                synonyms.append(lm.name())

        synonyms = (set(synonyms))
        words.extend(list(synonyms)[:2])
        synonyms = []

    return " ".join(words)
