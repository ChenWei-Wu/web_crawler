import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

title = soup.find_all('div' , 'title')

for i in range(len(title)):
	if(title[i].find('a') != None): #加入判斷條件式(如果拿到的不是已被刪除帖)
	
		#選出此頁的貼文資訊並提取出網址(Q2)
		################################
		href = 'https://www.ptt.cc' + title[i].find('a')['href']
		################################
		print(href)