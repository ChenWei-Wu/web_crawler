import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

title = soup.find_all('div' , 'title')

for i in range(len(title)):
	if(title[i].find('a') != None): 
	
		#---------------------------Q2---------------------------#
		##########################################################
		href = 'https://www.ptt.cc' + title[i].#答案寫這
		##########################################################
		print(href)