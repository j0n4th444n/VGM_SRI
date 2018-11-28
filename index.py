import json



index = {}

def start (json_request):

    json_data = json.loads(json_request)

    if json_data['action'] == 'create':
        create(json_data['data'])
    elif json_data['action'] == 'add':
        add(json_data['key'], json_data['value'])
    elif json_data['action'] == 'update':
        update(json_data['key'], json_data['value'])
    elif json_data['action'] == 'delete':
        delete(json_data['key'])
    elif json_data['action'] == 'terms':
        all_term_doc(json_data['key'])
    elif json_data['action'] == 'get':
        return get(json_data['key'])


def create(data):
    for elem in data:
        key = elem['key']
        value = elem['value']
        index[key] = value

def add(key , value):       # TODO: ver try, catch here
    try:
        if key in index:
            raise Exception()
        index[key] = value
    except(Exception):
            print("No se puede agregar " + key + " ya existe en el index")

def update(key, value):
    try:
        if key not in index:
            raise(Exception)
        index[key] = value
    except(Exception):
        print("El termino " + key + " no existe en el index" )


def delete(key):
    try:
        if key not in index:
            raise(Exception)
        index.pop(key)
    except(Exception):
        print("el termino " + key + " no existe")

def get(key):
    response = {}

    if key in index:
        response['success'] = True
        response['value'] = index[key]
    else:
        response['success'] = False
        response['value'] = None

    return json.dumps(response)

#devolver todos los terminos de un documento`
def all_term_doc(doc):
    response = {}
    terms = [term for term in index if (doc in index[term]['documents'])]
    response['terms'] = terms

    return json.dumps(response)
