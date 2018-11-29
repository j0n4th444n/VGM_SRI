import queue
import urllib3
import socket
import requests
import os
import sys
import re
from bs4 import BeautifulSoup, SoupStrainer

username = r'b.vera%40estudiantes.matcom.uh.cu'
password = r'T%40Ta30091992*'
host = "10.6.100.71"
port = 3128

proxies = {
    'http': f'http://{username}:{password}@{host}:{port}',
    'https': f'https://{username}:{password}@{host}:{port}'
}

def download(url,use_proxy):
    return requests.get(url, proxies=proxies).text if use_proxy else requests.get(url).text

def get_links(page,url):
    return re.findall('"((http)s?://.*?)"', page)

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

def create_name(folder):    
    return os.path.join(folder,str(len(os.listdir('crawling')))+".text")

def save_doc(url,text):
    with open(create_name('crawling'),'w', encoding='utf8', errors='ignore') as f:
        f.write(text)

def save_indexer(links):
    with open(create_name('ind_url'),'w', encoding='utf8', errors='ignore') as f:
        for link in links:
            f.write(link+"\n")

def crawler(seed_url,proxy = False,user_name = None,password = None,host_ip = None,port = None):
    l = []
    q = queue.Queue()
    for url in seed_url:
        q.put(url)
    while(not q.empty()):
        url = q.get()
        l.append(url)
        html = download(url,proxy)
        links = get_links(html,url)
        text = get_text_from_html(html)
        save_doc(url,text)
        for (link,form) in links:
            if link not in q.queue:
                q.put(link)
    save_indexer(l)

seed = ["https://stackoverflow.com/"]
crawler(seed,False,username,password,host,port)