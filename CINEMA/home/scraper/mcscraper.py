#To scrape ratings and comments from Metacritic

import requests
from bs4 import BeautifulSoup
import re

#To scrape the comments
def revprint(user):
	if user.find('span')!=None:
		return user.contents[1].text.strip()
	else:
		return user.text.strip()

#To get the url of the site
#url=input("URL:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
r=requests.get(url,headers=user_agent)

#To scrape the comments and score
def mc(url):
	r=requests.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')

	#Scrape the ratings
	metascore=soup.find('div',class_='ms_wrapper').find('a',class_='metascore_anchor').find('span').text+'/100'
	userscore=soup.find('div',class_='us_wrapper').find('a',class_='metascore_anchor').find('span').text+'/10'

	#Scrape comments
	soup=soup.find('div',class_='reviews pad_top2 subrow')
	#critic=soup.find('div', class_='critic_reviews2').find_all('div',class_='review_body')
	user=soup.find('div', class_='user_reviews2').find_all('div',class_='review_body')

	user1=user[0].span
	user2=user[len(user)-1].span

	"""print(metascore)
	print(userscore)
	print(user1.parent.parent.parent.parent.div.div.div.text+'/10')
	print(revprint(user1))
	print(user2.parent.parent.parent.parent.div.div.div.text+'/10')
	print(revprint(user2))"""
	rating1=user1.parent.parent.parent.parent.div.div.div.text+'/10'
	rating2=user2.parent.parent.parent.parent.div.div.div.text+'/10'
	return (metascore, userscore, rating1, revprint(user1), rating2, revprint(user2))

#print(mc(url))