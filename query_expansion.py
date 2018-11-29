# import modelo
#
# synonyms = []
#
# for syn in wn.synsets("home"):
#     for lm in syn.lemmas():
#              synonyms.append(lm.name())
# print (set(synonyms))
#
#
# cane_lemmas = wn.lemmas("hombre", lang="spa")
# print(cane_lemmas)
#
#
#
# resdef = wn.synset('ocean.n.1').definition()
# print (resdef)
import json
import modelo
import index
from langdetect import detect
from nltk.corpus import wordnet as wn



def start(json_request):

    data = json.loads(json_request)
    json_result = json.loads(modelo.request_query(data['query'], data['count'], data['similarity_techniques']))
    documents = [pair["document"] for pair in json_result['results']]

    relevant_words =  pseudo_Relevance_Feedback(documents)

    words = data['query'] + " " + relevant_words

    # TODO: SI LA QUERY ESTA EN INGLES HACEMOS TRABAJO CON SINONIMOS
    # if detect(data['query']) == 'en':
    #     words += expansion_synonyms(data['query'])

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

def expansion_synonyms(query):

    synonyms = []

    for syn in wn.synsets(query):
        for lm in syn.lemmas():
                 synonyms.append(lm.name())
    print (set(synonyms))



# expansion_synonyms("work")