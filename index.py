import json


__index = {}

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
    elif json_data['action'] == 'terms_frec':
        return __all_term_doc_frec(json_data['key'])
    elif json_data['action'] == 'get':
        return __get(json_data['key'])


def __create(data):
    for elem in data:
        key = elem['key']
        value = elem['value']
        __index[key] = value

def __add(key , value):       # TODO: ver try, catch here
    try:
        if key in __index:
            raise Exception()
        __index[key] = value
    except(Exception):
            print("No se puede agregar " + key + " ya existe en el __index")

def __update(key, value):
    try:
        if key not in __index:
            raise(Exception)
        __index[key] = value
    except(Exception):
        print("El termino " + key + " no existe en el __index" )


def __delete(key):
    try:
        if key not in __index:
            raise(Exception)
        __index.pop(key)
    except(Exception):
        print("el termino " + key + " no existe")

def __get(key):
    response = {}

    if key in __index:
        response['success'] = True
        response['value'] = __index[key]
    else:
        response['success'] = False
        response['value'] = None

    return json.dumps(response)


def __all_term_doc(doc):
    response = {}
    terms = [term for term in __index if (doc in __index[term]['documents'])]
    response['terms'] = terms

    return json.dumps(response)

def __all_term_doc_frec(doc):
    response = {}
    terms = [(term, __index[term]['documents'][doc]['tf']) for term in __index if (doc in __index[term]['documents'])]
    response['terms'] = terms

    return json.dumps(response)
