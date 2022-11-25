#Automatic scraper for Metacritic (To be run after mc.py)

import mysql.connector as db
import requests
from bs4 import BeautifulSoup
import unidecode
import re

user_agent={'User-agent':'Mozilla/5.0'}

mydb = db.connect(
  host="localhost",
  user="root",
  password="1879",
  database="CINEMA"
)

mycursor = mydb.cursor()
sql="UPDATE TITLES SET mc=%s WHERE (name=%s AND year=%s)"
req=requests.session()

mycursor.execute("SELECT name, year FROM TITLES WHERE mc IS NULL")

for mov in mycursor.fetchall():
	print('**********',mov[0])
	url="https://www.metacritic.com/movie/"+(re.sub(r'[\s]+',' ',re.sub(r"[\'\,\:\;\.\(\)\\\/\&\-]",'',unidecode.unidecode(mov[0])))).replace(' ','-').lower()+'-'+str(mov[1])
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	if soup.title.text=='404 Page Not Found - Metacritic - Metacritic':
		url=url[:-5]
		r=req.get(url,headers=user_agent)
		soup=BeautifulSoup(r.content,'html5lib')
		if soup.title.text=='404 Page Not Found - Metacritic - Metacritic':
			print(mov[0],mov[1])
			pass
		else:
			mycursor.execute(sql,(url,mov[0],mov[1]))
			#print('**********',mov[0])
	else:
		mycursor.execute(sql,(url,mov[0],mov[1]))
		#print('**********',mov[0])

mydb.commit()