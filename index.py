import json


index = {}

def start (json_request):

    json_data = json.loads(json_request)

    if json_data['action'] == 'create':
        __create(json_data['data'])
    elif json_data['action'] == 'add':
        __add(json_data['key'], json_data['value'])
    elif json_data['action'] == 'update':
        __update(json_data['key'], json_data['value'])
    elif json_data['action'] == 'delete':
        __delete(json_data['key'])
    elif json_data['action'] == 'terms':
        return __all_term_doc(json_data['key'])
    elif json_data['action'] == 'get':
        return __get(json_data['key'])


def __create(data):
    for elem in data:
        key = elem['key']
        value = elem['value']
        index[key] = value

def __add(key , value):       # TODO: ver try, catch here
    try:
        if key in index:
            raise Exception()
        index[key] = value
    except(Exception):
            print("No se puede agregar " + key + " ya existe en el index")

def __update(key, value):
    try:
        if key not in index:
            raise(Exception)
        index[key] = value
    except(Exception):
        print("El termino " + key + " no existe en el index" )


def __delete(key):
    try:
        if key not in index:
            raise(Exception)
        index.pop(key)
    except(Exception):
        print("el termino " + key + " no existe")

def __get(key):
    response = {}

    if key in index:
        response['success'] = True
        response['value'] = index[key]
    else:
        response['success'] = False
        response['value'] = None

    return json.dumps(response)


def __all_term_doc(doc):
    response = {}
    terms = [term for term in index if (doc in index[term]['documents'])]
    response['terms'] = terms

    return json.dumps(response)


# def __all_term_doc(doc):
#     response = {}
#     terms=[]
#     for term in index:
#         for dicc in index[term]['documents']:
#             if dicc['document']==doc:
#                 terms.append(term)
#                 break
#     response['terms'] = terms
#
#     return json.dumps(response)



# index={'uno':{'idf':4,
#               'documents':[{'document':"doc1",
#                             'if': 45,
#                             'weight':45
#                             }]
#               },
#         'dos':{'idf':4,
#               'documents':[{'document':"doc",
#                             'if': 45,
#                             'weight':45
#                             }]
#               }
#        }
#
# terms = __all_term_doc("doc1")
# print(terms)