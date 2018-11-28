import queue
import urllib3
import socket
import requests
import os
import sys
from urllib3 import ProxyManager, make_headers
from bs4 import BeautifulSoup, SoupStrainer

directory = os.getcwd()

def download(url,http):
    return http.request('GET',http).data

def get_links(page,url):
    list = []
    soup = BeautifulSoup(page)
    for link in soup.find_all('a'):
        list.append(link.get('href'))
    return list

def get_text_from_html(data):
    # removing js
    while(True):
        i = data.find('<script',0,len(data))
        if i == -1:
            break
        j = data.find('</script>',i,len(data))
        data = data.replace(data[i:j+9],' ',1)

    # removing CSS
    while(True):
        i = data.find('<style',0,len(data))
        if i == -1:
            break
        j = data.find('</style>',i,len(data))
        data = data.replace(data[i:j+8],' ',1)

    # removing Comments
    while(True):
        i = data.find('/*',0,len(data))
        if i == -1:
            break
        j = data.find('*/',i,len(data))
        data = data.replace(data[i:j+2],' ',1)

    soup = BeautifulSoup(data,"html5lib")
    return soup.get_text(strip=True,separator=' ')

def get_ip_from_host(url_host):
    try:
        ips = socket.gethostbyname_ex(url_host)
    except socket.gaierror:
        ips=[]
    return ips[0] if len(ips) > 0 else None

def replace_win_name(direction,url):
    """
    direction: True  -> convert url into windows folder name
    direction: False -> convert windows folder name into url
    """
    if direction:
        url = url.replace('/','_')
        url = url.replace(':','..')
        return url
    else:
        url = url.replace('_','/')
        url = url.replace('..',':')
        return url

def create_name():
    # ! remplacing special simbols
    d = os.path.join("crawling",str(len(os.listdir("crawling")))+".txt")
    return d

def save_doc(text):
    with open(create_name(),'w', encoding='utf8', errors='ignore') as f:
        f.write(text)

def crawler(seed_url,proxy = False,user_name = None,password = None,host_ip = None,port = None):
    dict = {}
    if proxy:
        default_headers = make_headers(proxy_basic_auth=user_name+':'+password)
        http = ProxyManager("https://"+ host_ip +":" +port, headers=default_headers)
    q = queue.Queue()
    for url in seed_url:
        q.put(url)

    while(not q.empty()):
        url = q.get()
        html = download(url,http)
        text = get_text_from_html(html)
        save_doc(text)
        for link in get_links(html,url):
            if link not in q.queue:
                q.put(link)

# with open('prueba.htm','r',encoding='utf8',errors='ignore') as f:
#     data =f.read()
# text = get_text_from_html(data)
# save_doc('asd',text)