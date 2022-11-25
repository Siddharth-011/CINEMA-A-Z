import mysql.connector as db
#import requests
#from bs4 import BeautifulSoup
#import unidecode
#import re

#user_agent={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Accept-Language':'en-us'}

mydb = db.connect(
  host="localhost",
  user="root",
  password="1879",
  database="CINEMA"
)

mycursor = mydb.cursor()
#sql="UPDATE TITLES SET rt=%s WHERE (name=%s AND year=%s)"
#req=requests.session()

sql="UPDATE TITLES SET rt=%s WHERE (name=%s AND year=%s)"
mycursor.execute("SELECT name, year FROM TITLES WHERE rt IS NULL")

for mov in mycursor.fetchall():
	print(mov[0],mov[1])
	url=input("URL:").strip()
	if url=="null":
		continue
	else:
		mycursor.execute(sql,(url,mov[0],mov[1]))

mydb.commit()