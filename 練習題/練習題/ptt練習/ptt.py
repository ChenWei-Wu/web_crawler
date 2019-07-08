import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

num = 0
first_dir='ptt//'
if os.path.exists(first_dir):
	shutil.rmtree(first_dir)
else:
	os.makedirs(first_dir)

#-----------------Q1-------------------#
#######################################
title = soup.
#######################################
#單獨進入各貼文
for i in range(len(title)):
	if(): #加入判斷條件式(如果拿到的不是已被刪除帖)
		#---------------------------Q2---------------------------#
		##########################################################
		href = 'https://www.ptt.cc' + title[i].
		##########################################################
			
		target = href
		req = requests.get(url=target,headers=headers)
		soup = BeautifulSoup(req.text,'html.parser')

		#-------------------------Q3-------------------------#
		######################################################
		content = soup.
		######################################################

		#輸出檔案
		file = open(first_dir+str(num+1)+'.txt','w', encoding = 'UTF-8')
		file.write(str(content))
		file.close()
		num+=1
		print('第'+str(num)+'篇文章下載完成')