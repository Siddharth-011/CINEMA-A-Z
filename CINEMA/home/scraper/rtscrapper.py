#To scrape comments and rating from Rotten Tomatoes

import requests
from bs4 import BeautifulSoup
import re

#To get the url of the site
#url=input("URL:")
#year=input("Year:")
#typ=input("Type:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
req=requests.Session()

key={'vudu':'Vudu', 'peacock':'Peacock', 'amc-plus-us':'AMC+', 'netflix':'Netflix', 'hulu':'Hulu', 'amazon-prime-video-us':'Amazon Prime', 'disney-plus-us':'Disney+', 'hbo-max':'HBO-Max', 'paramount-plus-us':'Paramount+', 'apple-tv-plus-us':'Apple TV+', 'showtime':'Showtime', 'itunes':'Apple TV'}

#Scrape Rating, year(for shows) and where to watch
def rt(url,year,typ):
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')

	#Where to watch
	w2w=soup.find('bubbles-overflow-container',{'data-qa':'section:w2w-items'}).contents
	w2wlist=[]
	#print('Watch here :')
	for item in w2w:
		try:
			#print(item['affiliate'],item['href'])
			w2wlist.append({'platform':key[item['affiliate']], 'href':item['href']})
		except:
			pass

	#Rating
	if int(typ)==0:
		#Year
		score=soup.find('h1',class_='title').span.text.strip()
		#print('Year -',score)
		year=score

		score=soup.find('div',{'data-qa':'tomatometer-container'})
		#print('Critics -',score.find('span', {'data-qa':'tomatometer'}).text.strip())
		criticscore=score.find('span', {'data-qa':'tomatometer'}).text.strip()
		score=score.parent
		#print('Audience -',score.find('span', {'data-qa':'audience-score'}).text.strip())
		userscore=score.find('span', {'data-qa':'audience-score'}).text.strip()

		return (w2wlist, year, criticscore, userscore)
	else:
		score=soup.find('score-board')
		#print('Critics -',score['tomatometerscore'])
		criticscore=score['tomatometerscore']+'%'
		#print('Audience -',score['audiencescore'])
		userscore=score['audiencescore']+'%'

		return (w2wlist, year, criticscore, userscore)
	
#print(rt(url,year,typ))