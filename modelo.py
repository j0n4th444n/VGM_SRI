import os
import glob
import sys
import math
import json
import index
from nltk import FreqDist
import text_proc




def model(json_request):

	data = json.loads(json_request)

	if data['action'] == 'build':
		request_build(data['path'])
	elif data['action'] == 'query':
		return request_query(data['query'], data['count'], data['similarity_techniques'])


# TODO: proceamiento de texto
def request_build(path):

	data = []

	if 'win' in sys.platform:
		_path = path + "\**"
	else:
		_path = path + "/**"

	if os.path.exists(path):
		# pdf_docs = glob.glob(os.path.join(_path, "*.pdf"), recursive=True)
		# docx_docs = glob.glob(os.path.join(_path, "*.docx"), recursive=True)
		txt_docs = glob.glob(os.path.join(_path, "*.txt"), recursive=True)
		docs =  txt_docs #+ docx_docs + pdf_docs

		docs_text = [(doc_path,read_doc(doc_path),0) for doc_path in docs]
		vector = get_vector(docs_text)

		#crear la estructura 'docs_text' que se utiliza para poder calcular los minterms d cada documento
		for index_doc in range(len(docs_text)):

			json_process = json.dumps({'action':'process', 'data':docs_text[index_doc][1]})
			terms = json.loads(text_proc.text_work(json_process))['terms']

			minterm_of_doc = get_minterm_of_document(vector, terms)
			docs_text[index_doc] = (docs_text[index_doc][0], terms, minterm_of_doc)

		#Creando el indice
		for doc in docs_text:
			terms = doc[1]
			doc_name = os.path.basename(doc[0])
			append_terms(doc_name, terms, data, minterm_doc=doc[2], vector= vector )

		append_idfs(data, len(docs))
		append_weights(data)

		json_process = json.dumps({'action':'create', 'data':data})
		index.start(json_process)

	else: raise Exception("The path is not correct")

# TODO: proceamiento de texto
#TODO poner las otras medidas
#TODO quitar palabras que no son de ningun doc
def request_query(query, count_doc, similarity_techniques):

	json_process = json.dumps({'action': 'process', 'data': query})
	query_terms = json.loads(text_proc.text_work(json_process))['terms']

	query_data = []
	vector = {query_terms[index_term]:index_term for index_term in range(len(query_terms)) }

	#Construir el indice de la query
	append_terms('query',query_terms,query_data,"0",vector)
	append_idfs(query_data, 1)
	append_weights(query_data)

	docs = get_docs_from_query(query_terms)
	dicc_ranking = similarity_cosine(query_data, docs) if similarity_techniques == 0 else similarity_cosine(query_data, docs)

	result= list(zip(dicc_ranking.keys(), dicc_ranking.values()))
	result.sort(key=lambda x: x[1], reverse=True)
	result = result[:count_doc]

	return json.dumps({'action':'report', 'sucess':True,'results':[{'document':dc, 'match':val} for dc, val in result]})

##########################################################
#################### CONSTRUIR INDEX #####################
##########################################################

def append_terms(doc, terms, data, minterm_doc,vector):

	tf = FreqDist(terms)
	max_tf = max(tf.values()if len(tf)>0 else [0])

	for term in tf.keys():
		normalize_tf = tf[term] / max_tf
		new_doc = {'tf': normalize_tf,
				   'weight': 0,
				   'minterm':minterm_doc}
		in_data = False
		for term_data in data:
			if term == term_data['key']:

				#update
				term_data['value']['documents'][doc] = new_doc
				in_data = True
				break

		if not in_data:
			# add
			data.append({'key': term,
						 'value': {'idf':0,
									'documents': {doc:new_doc},
									'index_in_vector': vector[term]}})

def append_idfs(data, N):
	for term in data:
		term['value']['idf'] = math.log10((N / len(term['value']['documents'])) + 1)

def append_weights(data):

	for term in data:
		for doc in term['value']['documents'].keys():
			term['value']['documents'][doc]['weight'] = get_weight_term_doc(data, term, (doc,term['value']['documents'][doc]))

#TODO: Index doc[terms]
#TODO values = value
def get_weight_term_doc(data, term, doc):
	# json_get_request = index.start(json.dumps({'action':'get', 'key':term}))
	# dic_get_request = json.loads(json_get_request)


	term = term['value']

	weight = doc[1]['tf'] * term['idf']

	ter_doc = [tm for tm in data if doc[0] in tm['value']['documents'].keys()]
	list_for_sum = [(tm['value']['idf'] * tm['value']['documents'][dc]['tf']) ** 2 for tm in ter_doc for  dc in tm['value']['documents'] if
					dc == doc[0]]

	doc_norm = math.sqrt(sum(list_for_sum))

	return weight / doc_norm

#TODO: proceamiento de texto
def get_vector(docs_text):

	all_docs_together = ""
	vector_of_terms = []
	i=0
	for doc in docs_text:
		print(os.path.basename(doc[0]))
		i+=1
		json_process = json.dumps({'action': 'process', 'data': doc[1]})
		json_request =json.loads(text_proc.text_work(json_process))
		vector_of_terms = vector_of_terms + json_request['terms']
	vector_of_terms = list(set(vector_of_terms))
	return  {vector_of_terms[index_term]: index_term for index_term in range(len(vector_of_terms))}

def get_minterm_of_document(vector, doc_terms):
	minterm = ""
	for tm in vector.keys():
		if tm in doc_terms:
			minterm += "1"
		else:
			minterm += "0"

	return minterm

##########################################################

##########################################################
############### PROCESAMIENTO DOCUMENTOS #################
##########################################################

def get_docs_from_query(query_terms):

	docs = {}
	for term in query_terms:
		json_respons = json.loads(index.start(json.dumps({'action':'get', 'key':term})))
		if json_respons['success']:
			term_value = json_respons['value']
			for doc in term_value['documents'].keys():
				if doc not in docs:
					docs[doc] = {'terms': {term: 0}, 'weights': [term_value['documents'][doc]['weight']]}
				else:
					docs[doc]['terms'][term] = len(docs[doc]['weights'])
					docs[doc]['weights'].append(term_value['documents'][doc]['weight'])

	return docs

def read_doc(doc_path):
	return read_txt(doc_path) if doc_path.endswith('.txt') else read_pdf(doc_path) if doc_path.endswith('.pdf') else\
		read_html(doc_path) if doc_path.endswith('.html') else read_docx(doc_path)

def read_txt(txt_path):
	with open(txt_path, "r", encoding="utf8", errors="ignore") as f:
		document = f.read()
		f.close()
		return document

# TODO: PDF
def read_pdf(pdf_path):
	pass

#TODO: HTML
def read_html(html_path):
	pass

#TODO: DOCX
def read_docx(docx_path):
	pass

##########################################################

##########################################################
###################### FORMULAS MVG ######################
##########################################################

#TODO:EXPLICAR
def term_i_Dot_term_j(term_i, term_j):
	result = 0
	analized_minterm = []
	for doc_tm_i in term_i['documents']:
		if term_i['documents'][doc_tm_i]['minterm'] not in analized_minterm and \
				term_i['documents'][doc_tm_i]['minterm'][term_i['index_in_vector']] == '1' and term_i['documents'][doc_tm_i]['minterm'][term_j['index_in_vector']] == '1':
			result += ci_r(term_i,term_i['documents'][doc_tm_i]['minterm'])*ci_r(term_j,term_i['documents'][doc_tm_i]['minterm'])
			analized_minterm.append(term_i['documents'][doc_tm_i]['minterm'])

	for  doc_tm_j in term_j['documents']:
		if term_j['documents'][doc_tm_j]['minterm'] not in analized_minterm and \
				term_j['documents'][doc_tm_j]['minterm'][term_i['index_in_vector']] == '1' and term_j['documents'][doc_tm_j]['minterm'][term_j['index_in_vector']] == '1':
			result += ci_r(term_i,term_j['documents'][doc_tm_j]['minterm'])*ci_r(term_j,term_j['documents'][doc_tm_j]['minterm'])
			analized_minterm.append(term_j['documents'][doc_tm_j]['minterm'])

	return result

def ci_r(term_i, minterm_r):
	return sum([term_i['documents'][doc]['weight'] for  doc in term_i['documents'] if term_i['documents'][doc]['minterm'] == minterm_r ])

##########################################################

##########################################################
################### SIMILARITY METRICS ###################
##########################################################

def similarity_cosine(query_data, docs):
	dicc_ranking = {}

	for doc in docs.keys():
		numerador = 0
		sum_weight_in_doc =0
		sum_weight_in_query =0
		for tm_query_i in query_data:
			for tm_query_j in query_data:
				if tm_query_i['key'] in docs[doc]['terms'].keys():
					weight_query_i = tm_query_i['value']['documents']['query']['weight']
					index_weight_data = docs[doc]['terms'][tm_query_i['key']]
					weight_doc_j = docs[doc]['weights'][index_weight_data]
					tmI = {}
					tmJ = {}
					tm = get_from_index(tm_query_i['key'])
					if tm['success']:
						tmI = tm['value']
					tm = get_from_index(tm_query_j['key'])

					if tm['success']:
						tmJ = tm['value']
					tmI_dot_tmJ = term_i_Dot_term_j(tmI, tmJ)

					numerador += weight_query_i * weight_doc_j * tmI_dot_tmJ

			if tm_query_i['key'] in docs[doc]['terms'].keys():


				weight_query = tm_query_i['value']['documents']['query']['weight']
				sum_weight_in_query += weight_query **2

		json_request = json.dumps({'action':'terms', 'key':doc})
		json_responsive = index.start(json_request)
		result = json.loads(json_responsive)
		terms_in_doc = result['terms']

		for tm_doc in terms_in_doc:
			tm = get_from_index(tm_doc)['value']
			for d in tm['documents']:
				if d == doc:
					sum_weight_in_doc += tm['documents'][d]['weight']**2

		denominador = math.sqrt(sum_weight_in_doc*sum_weight_in_query)

		dicc_ranking[doc] = numerador/denominador

	return dicc_ranking

def similarity_inner_product(query_data, docs):
	pass

def similarity_dice(query_data, docs):
	pass

def similarity_jaccard(query_data, docs):
	pass

def similarity_vectorial_model(query_data, docs):
	dicc_ranking = {}

	for doc in docs.keys():
		for tm_query in query_data:
			if tm_query['key'] in docs[doc]['terms'].keys():

				weight_query = tm_query['value']['documents'][0]['weight']
				index_weight_data = docs[doc]['terms'][tm_query['key']]
				weight_data = docs[doc]['weights'][index_weight_data]
				if doc not in dicc_ranking:
					dicc_ranking[doc] = weight_query * weight_data
				else:
					dicc_ranking[doc] += weight_query * weight_data
	return dicc_ranking

##########################################################

def get_from_index(term):
	return json.loads(index.start(json.dumps({'action':'get', 'key':term})))