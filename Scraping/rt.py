import mysql.connector as db
import requests
from bs4 import BeautifulSoup
import unidecode
import re

user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}

mydb = db.connect(
  host="localhost",
  user="root",
  password="1879",
  database="CINEMA"
)

mycursor = mydb.cursor()
sql="UPDATE TITLES SET rt=%s WHERE (name=%s AND year=%s)"
req=requests.session()

mycursor.execute("SELECT name, year FROM TITLES WHERE rt IS NULL")

for mov in mycursor.fetchall():
	print('**********',mov[0])
	url="https://www.rottentomatoes.com/m/"+re.sub(r"[\'\,\:\;\.\-\(\)]",'',unidecode.unidecode(mov[0].replace(' ','_'))).lower()+'_'+str(mov[1])
	r=req.get(url,headers=user_agent)
	soup=BeautifulSoup(r.content,'html5lib')
	if soup.title.text=='Rotten Tomatoes: Movies - Rotten Tomatoes':
		url=url[:-5]
		r=req.get(url,headers=user_agent)
		soup=BeautifulSoup(r.content,'html5lib')
		if soup.title.text=='Rotten Tomatoes: Movies - Rotten Tomatoes':
			print(mov[0],mov[1])
			pass
		else:
			mycursor.execute(sql,(url,mov[0],mov[1]))
			#print('**********',mov[0])
	else:
		mycursor.execute(sql,(url,mov[0],mov[1]))
		#print('**********',mov[0])

mydb.commit()