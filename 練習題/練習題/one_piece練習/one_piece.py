#前置步驟(不用改)
import requests
from bs4 import BeautifulSoup
import string
import os
import time
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/comic/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
folder_path = 'one_piece/'

# 建立 one_piece 資料夾(不用改)
if os.path.exists(folder_path):
	shutil.rmtree(folder_path)
else:
	os.makedirs(folder_path)

#--------------------Q1答案--------------------#
##############################################

a_tags = soup.#答案寫這

##############################################

j = 0
now = 0
for a in a_tags :
	now += 1
	#建立 第n話 資料夾(不用改)
	folder_path = 'one_piece/' + a.string.encode(req.encoding).decode('utf-8') + '/'
	if os.path.exists(folder_path):
		shutil.rmtree(folder_path)
	else:
		os.makedirs(folder_path)

	
	#--------------------Q2答案--------------------#
	################################################

	ep_url = 'https://one-piece.cn/' + #答案寫這

	################################################
	
	#進入連結(不用改)
	req = requests.get(url = ep_url , headers = headers)
	soup = BeautifulSoup(req.text,'html.parser')
	
	
	#--------------------Q3答案--------------------#
	################################################

	all_p = soup.#答案寫這

	################################################
	
	i = 0
	for p in all_p :
		i += 1
		if(p.img != None):
			
			#---------------------Q4答案-------------------#
			################################################

			src = p.#答案寫這

			################################################
			
			#進行存取  下載(不用改)
			img_byte = requests.get(src).content
			file = open(folder_path + str(i).zfill(2) + '.png' , 'wb')
			file.write(img_byte)
			file.close()
			
			#匯報進度(不用改)
			print('進度:'+str(now)+'/'+str(len(a_tags))+'   '+str(i)+'/'+str(len(all_p)))
			
