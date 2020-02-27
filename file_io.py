"""
Mode    Description

'r' This is the default mode. It Opens file for reading.
'w' This Mode Opens file for writing. 
If file does not exist, it creates a new file.
If file exists it truncates the file.
'x' Creates a new file. If file already exists, the operation fails.
'a' Open file in append mode. 
If file does not exist, it creates a new file.
't' This is the default mode. It opens in text mode.
'b' This opens in binary mode.
'+' This will open a file for reading and writing (updating)

'rb'  read binary
'wb'  write binary
'ab'  append binary
'rb+' read + write binary
'wb+' read + write binary
'ab+' append + read binary

"""

import glob 

papers_dir = '.'
docs_path = glob.glob(papers_dir+"*.pdf")

############ Download pdf ############
import requests

def download_pdf(url):
    file = requests.get(url, allow_redirects=True)
    name = url[url.rfind('/')+1:]
    with open(f'./path_to_save/{name}', 'wb') as out:
        out.write(file.content)