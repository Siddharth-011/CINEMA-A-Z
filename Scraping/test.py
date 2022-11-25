"""
import requests
from bs4 import BeautifulSoup

imdb=requests.session()
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url="https://www.imdb.com/title/tt15791034/?ref_=hm_fanfav_tt_t_5_pd_fp1"#input("URL: ")

movies=[]
movies.append("Barbarian")

def recIMDb(url):
	#scrape
	#print('Inside')
	r=imdb.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	soup=soup.find('section',{'data-testid':'MoreLikeThis'}).find('div',class_='ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--nowrap ipc-shoveler__grid').find_all('a',class_='ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable')
	#print(soup.prettify())
	for i in range(4):
		movie=soup[i]
		mov=movie.find('span').text
		if mov not in movies:
			print(mov)
			movies.append(mov)
			recIMDb('http://www.imdb.com'+movie['href'])

recIMDb(url)
print(movies)
"""

import time

#Time in hours (1 unit = 2 hours)
print(round(int(time.time())/7200))