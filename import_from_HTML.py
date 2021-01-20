import requests
from bs4 import BeautifulSoup

getpage= requests.get('http://www.learningaboutelectronics.com')

getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

all_id_para1= getpage_soup.findAll('p', {'id':'para1'})

for para in all_id_para1:
    print (para)
