import requests
from bs4 import BeautifulSoup
import mysql.connector

imdb=requests.session()
user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}

#Enter teh URL you want to scrape
#url="https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=,2022-11-22&view=simple&sort=num_votes,desc&count=250"
url="https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=,2022-11-22&view=simple&sort=num_votes,desc&count=250&start=501&ref_=adv_nxt"
#url="https://www.imdb.com/search/title/?title_type=tv_series&release_date=,2022-11-22&view=simple&sort=num_votes,desc&count=250"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1879",
  database="CINEMA"
)
mycursor=mydb.cursor()
#Movies
sql="INSERT INTO TITLES (name, year, imdb, type, cast) VALUES (%s, %s, %s, 1, %s)"
#Shows
#sql="INSERT INTO TITLES (name, year, imdb, type, cast) VALUES (%s, %s, %s, 0, %s)"

#Type=True #for movies
Type=False #for shows

r=imdb.get(url,headers=user_agent)
soup=BeautifulSoup(r.content,'html5lib')
soup=soup.find('div',class_='lister-list').find_all('span',class_='lister-item-header')

for movie in soup:
	movie=movie.find_all('span')[1]
	cast=movie['title'].strip()
	year=movie.find('span').text.strip()
	year=int(year[len(year)-5:len(year)-1])
	movie=movie.find('a')
	link="https://imdb.com"+movie['href'].strip()
	name=movie.text.strip()
	print(name)
	mycursor.execute(sql,(name, year, link, cast))

mydb.commit()