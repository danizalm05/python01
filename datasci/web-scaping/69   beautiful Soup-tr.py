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

print("Headers of table\n ----------------------\n\n")
for header in table.find('tr').find_all('th'):
  headers.append(header.text)
  print('header= ' , header.text)

print(" Cells of table\n---------------------\n")
# Then go through all the rows except the first one
for row in table.find_all('tr')[1:]:
      print("\n++++++\n")
      values = []  
    
     # And get the column cells, the first one being inside a th-tag
      for col in row.find_all(['th','td']):
          print(col.text)
          values.append(col.text) 
      
      
for row in rows:
    
  print(i,"  ",row,'\n')
 
  i=i+1