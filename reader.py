import os
import PyPDF2
import re
from itertools import accumulate
from enum import Enum
from bs4 import BeautifulSoup, SoupStrainer
from PyPDF2 import PdfFileReader
from docx import Document


class Doc(Enum):
    web = 1
    pdf = 2
    word = 3

class Lang(Enum):
    ES = 1
    EN = 2

# ! funciona perfect
def __read_pdf_in_path(path,lang):
    with open(path,'rb') as f:
        if lang is Lang.ES:
            pdf = PdfFileReader(f)
            text = ''
            for i in range(pdf.getNumPages()):
                temp = (pdf.getPage(i).extractText()).replace('\n','ÿ')
                temp2 = temp[0] if temp[0] != 'ÿ' else ''
                for j in range(1,len(temp),1):
                    if temp[j] != 'ÿ':
                        temp2 += temp[j]
                    continue
                text += temp2
            return text
        elif lang is Lang.EN:
            pdf = PdfFileReader(f)
            text = ''
            for i in range(pdf.getNumPages()):
                text += pdf.getPage(i).extractText() + " "
            return text

# ! funciona perfect
def __read_web_in_path(path):
    with open(path,'r',encoding='utf8',errors='ignore') as f:
        data = f.read()
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

# ! funciona perfect
def __read_word_in_path(path):
    document = Document(path)
    text = ""
    for para in document.paragraphs:
        text += para.text + "\n"
    return text

def __read_txt_in_path(txt_path):
    with open(txt_path, "r", encoding="utf8", errors="ignore") as f:
        document = f.read()
        return document

def read(path : str,lang=None):
    if os.path.isfile(path):
        # ! PDF (.pdf)
        if path.endswith('.pdf') is Doc.pdf:
            return __read_pdf_in_path(path,lang)
        # ! Word Document (.docx)
        elif path.endswith('.doc') or path.endswith('.docx'):
            return __read_word_in_path(path)
        # ! Web Page(.htm .html)
        elif path.endswith('.htm') or path.endswith('.html'):
            return __read_web_in_path(path)
        # ! Text Documents (.txt)
        elif path.endswith('.txt'):
            return __read_txt_in_path(path)

# print(read("C:\\Users\\jonathaaan\\Desktop\\testing\\2018-2019. Orientaciones del proyecto de SI.pdf",Doc.pdf,Lang.ES))
# print(read("C:\\Users\\jonathaaan\\Desktop\\testing\\to_print-mining-the-news.pdf",Doc.pdf,Lang.EN))
# print(read("C:\\Users\\jonathaaan\\Desktop\\testing\\test_ibm3.html",Doc.web))
# print(read("C:\\Users\\jonathaaan\\Desktop\\testing\\test.docx",Doc.word))