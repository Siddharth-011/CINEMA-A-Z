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

#key={'vudu':'Vudu', 'peacock':'Peacock', 'amc-plus-us':'AMC+', 'netflix':'Netflix', 'hulu':'Hulu', 'amazon-prime-video-us':'Amazon Prime', 'disney-plus-us':'Disney+', 'hbo-max':'HBO-Max', 'paramount-plus-us':'Paramount+', 'apple-tv-plus-us':'Apple TV+', 'showtime':'Showtime', 'itunes':'Apple TV'}
key={'vudu':'v', 'peacock':'p', 'amc-plus-us':'amc', 'netflix':'nf', 'hulu':'h', 'amazon-prime-video-us':'ap', 'disney-plus-us':'dp', 'hbo-max':'hm', 'paramount-plus-us':'pp', 'apple-tv-plus-us':'atp', 'showtime':'s', 'itunes':'a'}

#Scrape Rating, year(for shows) and where to watch
def rt(url,year,typ):
	w2wdict={'v':None, 'p':None, 'amc':None, 'nf':None, 'h':None, 'ap':None, 'dp':None, 'hm':None, 'pp':None, 'atp':None, 's':None, 'a':None}
	if url==None:
		w2wdict.update({'seasoninfo':None, 'rt1':rt1,'rt2':rt2, 'year':year, 'r1rt':criticscore, 'r2rt':userscore, 'type':typ})
		return w2wdict
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')

	#Where to watch
	w2w=soup.find('bubbles-overflow-container',{'data-qa':'section:w2w-items'}).contents
	#print('Watch here :')
	i=0
	for item in w2w:
		try:
			#print(item['affiliate'],item['href'])
			w2wdict[key[item['affiliate']]]=item['href']
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

		soup=soup.find('section', id='seasonList').find_all('season-list-item')
		seasoninfo=""
		for ssn in soup:
			seasoninfo=seasoninfo+'[@#]'+ssn['seasontitle']+' - '+ssn['tomatometerscore']+'%'

		seasoninfo=seasoninfo[4:]

		dict_={'seasoninfo': seasoninfo, 'rt1':None,'rt2':None, 'year':year, 'r1rt':criticscore, 'r2rt':userscore, 'type':typ}
		dict_.update(w2wdict)
		return dict_
	else:
		score=soup.find('score-board')
		#print('Critics -',score['tomatometerscore'])
		criticscore=score['tomatometerscore']+'%'
		#print('Audience -',score['audiencescore'])
		userscore=score['audiencescore']+'%'

		#Scrape Critic scores
		r=req.get(url+'/reviews?sort=fresh',headers=user_agent)
		soup=BeautifulSoup(r.content,'html5lib')
		try:
			rt1=soup.find('div',class_='the_review').text.strip()
		except:
			rt1=None

		r=req.get(url+'/reviews?sort=rotten',headers=user_agent)
		soup=BeautifulSoup(r.content,'html5lib')
		try:
			rt2=soup.find('div',class_='the_review').text.strip()
		except:
			rt2=None

		dict_={'seasoninfo':None, 'rt1':rt1,'rt2':rt2, 'year':year, 'r1rt':criticscore, 'r2rt':userscore, 'type':typ}
		dict_.update(w2wdict)
		return dict_
	
#print(rt(url,year,typ))