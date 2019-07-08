import requests
from bs4 import BeautifulSoup
import string
import os
import time
import shutil
#前置步驟(不用改)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/comic/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

a_tags = soup.find('div' , id = 'chapter12').find_all('a')

for a in a_tags:

	#---------------------Q2--------------------#
	#############################################

	ep_url = '網址缺的部分' + 
	
	#############################################
	print(ep_url)