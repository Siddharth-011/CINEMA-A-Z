#To scrape comments and rating from Rotten Tomatoes

import requests
from bs4 import BeautifulSoup
import re

#To get the url of the site
url=input("URL:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
req=requests.Session()

#Scrape Rating
def rt(url):
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')

	#Where to watch
	w2w=soup.find('bubbles-overflow-container',{'data-qa':'section:w2w-items'}).contents
	print('Watch here :')
	for item in w2w:
		try:
			print(item['affiliate'],item['href'])
		except:
			pass

	#Rating
	score=soup.find('score-board')
	if score==None:
		#Year
		score=soup.find('h1',class_='title').span.text.strip()
		print('Year -',score)

		score=soup.find('div',{'data-qa':'tomatometer-container'})
		print('Critics -',score.find('span', {'data-qa':'tomatometer'}).text.strip())
		score=score.parent
		print('Audience -',score.find('span', {'data-qa':'audience-score'}).text.strip())
	else:
		print('Critics -',score['tomatometerscore'])
		print('Audience -',score['audiencescore'])
	
rt(url)