#To scrape comments, rating, genre and summary from IMDb

import requests
from bs4 import BeautifulSoup
import re

#To get the url of the site
url=input("URL:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
req=requests.Session()

#Scrape genre

#Scrape runtime

#Scrape summary

#Scrape language

#Scrape Rating
def imdb(url):
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	#Img
	img=soup.find('img',class_='ipc-image')['src']
	print(img)

	#More like this
	mlt=soup.find('section',{'data-testid':'MoreLikeThis'}).contents[1].contents[1].contents
	print('More Like This:-')
	for title in mlt:
		title=title.div.contents
		print(title[1].img['alt'],title[1].img['src'])
		print(title[2]['href'])

	#Language
	lang=soup.find('li',{'data-testid':'title-details-languages'}).a.text
	print('Language -',lang)

	#Runtime
	run=soup.find('li',{'data-testid':'title-techspec_runtime'}).div.text
	print('Runtime -',run)

	#Genre
	soup=soup.find('div',{'data-testid':'genres'})
	temp=soup.find_all('a')
	print('Genre :-')
	for genre in temp:
		print(genre.text)

	#Plot/Summary
	soup=soup.parent
	temp=soup.find('div',{'data-testid':'plot'}).find('span',{'data-testid':'plot-xl'}).text
	print('Plot -',temp)

	#Rating
	soup=soup.parent.find('div',{'data-testid':'hero-rating-bar__aggregate-rating__score'}).find('span').text
	print('Rating - '+soup+'/10')

#Scrape Comments
def comments(url):
	print('Review 1')
	r=req.get(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=desc',headers=user_agent)
	print(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=desc')
	soup=BeautifulSoup(r.content,'html5lib')
	soup=soup.find('div',class_='lister-list').find('div',class_='lister-item-content')
	print(soup.span.span.text,'/10')
	print('Heading -',soup.a.text.strip())
	print('Review -',soup.find('div',class_='content').div.text)
	print('Review 2')
	r=req.get(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=asc',headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	soup=soup.find('div',class_='lister-list').find('div',class_='lister-item-content')
	print(soup.span.span.text,'/10')
	print('Heading -',soup.a.text.strip())
	print('Review -',soup.find('div',class_='content').div.text)

imdb(url)
comments(url)