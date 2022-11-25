#To scrape comments, rating, genre and summary from IMDb

import requests
from bs4 import BeautifulSoup
import re

#To get the url of the site
#url=input("URL:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
req=requests.Session()

#Scrape genre
#Scrape runtime
#Scrape summary
#Scrape language
#Scrape Rating
def imdbsite(url):
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')

	#Img
	img=soup.find('img',class_='ipc-image')['src']
	#print(img)

	#More like this
	mlt=soup.find('section',{'data-testid':'MoreLikeThis'}).contents[1].contents[1].contents
	#print('More Like This:-')
	mltlist=[]
	for title in mlt:
		title=title.div.contents
		#print(title[1].img['alt'],title[1].img['src'])
		#print(title[2]['href'])
		mltlist.append({'img-src':title[1].img['src'], 'href':title[2]['href'][7:17]})

	#Language
	lang=soup.find('li',{'data-testid':'title-details-languages'}).a.text
	#print('Language -',lang)

	#Runtime
	runtime=soup.find('li',{'data-testid':'title-techspec_runtime'}).div.text
	#print('Runtime -',runtime)

	#Genre
	soup=soup.find('div',{'data-testid':'genres'})
	temp=soup.find_all('a')
	#print('Genre :-')
	genre=""
	for genre_ in temp:
		genre=genre+genre_.text+', '
	genre=genre[:-2]

	#Plot/Summary
	soup=soup.parent
	plot=soup.find('div',{'data-testid':'plot'}).find('span',{'data-testid':'plot-xl'}).text.strip()
	#print('Plot -',plot)

	#Rating
	soup=soup.parent.find('div',{'data-testid':'hero-rating-bar__aggregate-rating__score'}).find('span').text
	#print('Rating - '+soup+'/10')
	rating=soup+'/10'

	return [{'img':img, 'mlt':mltlist, 'lang':lang, 'runtime':runtime, 'genre':genre, 'plot':plot, 'score':rating}]

#Scrape Comments
def comments(url):
	#print('Review 1')
	r=req.get(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=desc',headers=user_agent)
	#print(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=desc')
	soup=BeautifulSoup(r.content,'html5lib')
	soup=soup.find('div',class_='lister-list').find('div',class_='lister-item-content')
	#print(soup.span.span.text+'/10')
	rating1=soup.span.span.text+'/10'
	#print('Heading -',soup.a.text.strip())
	heading1=soup.a.text.strip()
	#print('Review -',soup.find('div',class_='content').div.text)
	review1=soup.find('div',class_='content').div.text.strip()
	
	#print('Review 2')
	r=req.get(re.sub(r'\?.*$','',url)+'reviews?sort=userRating&dir=asc',headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	soup=soup.find('div',class_='lister-list').find('div',class_='lister-item-content')
	#print(soup.span.span.text+'/10')
	rating2=soup.span.span.text+'/10'
	#print('Heading -',soup.a.text.strip())
	heading2=soup.a.text.strip()
	#print('Review -',soup.find('div',class_='content').div.text)
	review2=soup.find('div',class_='content').div.text.strip()

	return [rating1, heading1, review1, rating2, heading2, review2]

def imdb(url):
	return imdbsite(url)+comments(url)

#print(imdb(url))