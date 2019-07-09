#前置步驟(不用改)
import requests
from bs4 import BeautifulSoup
import string
import os
import time
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/post/10903/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#---------------------Q3--------------------#
#############################################

all_p = soup.#答案寫這

#############################################

for p in all_p:
	print(p.encode(req.encoding).decode('utf-8'))