import requests
from bs4 import BeautifulSoup

url = 'https://www.w3docs.com/learn-html/html-table-tag'
url1 = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
r = requests.get(url)

html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')

tag='table'

first_tag = html_soup.find(tag)
print("name = ",first_tag.name) 
table = html_soup.find('table')
headers = []
rows = table.find_all('tr')
i=0
#  find header of table
for header in table.find('tr').find_all('th'):
  headers.append(header.text)
  print('header= ' , header.text)
for row in rows:
    
  print(i,"  ",row,'\n')
 
  i=i+1