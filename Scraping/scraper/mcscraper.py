#To scrape ratings and comments from Metacritic

import requests
from bs4 import BeautifulSoup
import re

def revprint(user):
	if user.find('span')!=None:
		print(user.contents[1].text.strip())
	else:
		print(user.text.strip())

#To get the url of the site
url=input("URL:")
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}
r=requests.get(url,headers=user_agent)

soup=BeautifulSoup(r.content,'html5lib')

#Scrape the ratings
temp=soup.find('div',class_='ms_wrapper').find('a',class_='metascore_anchor').find('span').text
temp2=soup.find('div',class_='us_wrapper').find('a',class_='metascore_anchor').find('span').text
print(temp)
print(temp2)

#Scrape comments
soup=soup.find('div',class_='reviews pad_top2 subrow')
#critic=soup.find('div', class_='critic_reviews2').find('div',class_='summary').find('a').text.strip()
user=soup.find('div', class_='user_reviews2').find_all('div',class_='review_body')#.find('div',class_='review_body').find('span').text.strip()
#critic=re.sub(r"\s\s+"," ",critic)
#user=re.sub(r"\s\s+"," ",user)
#print(critic)


user1=user[0].span
user2=user[len(user)-1].span

print('Review 1 -', user1.parent.parent.parent.parent.div.div.div.text)
revprint(user1)
print('Review 2 -', user2.parent.parent.parent.parent.div.div.div.text)
revprint(user2)