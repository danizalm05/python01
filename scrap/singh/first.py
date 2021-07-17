# Web Scraping with Python: Collecting Data from the Modern Web - O'Reilly Media
# https://www.youtube.com/watch?v=U7tN6Zs2UY4&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=6
# https://www.youtube.com/watch?v=GC890_Rco3g&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=7


from bs4 import BeautifulSoup

from urllib.request import urlopen
from urllib.error import HTTPError


def getTitle(url):
 try:
  html = urlopen(url)
 except HTTPError as e:
  return None

 try:
  Parser = 'html.parser' # 'html5lib'   'lxml' # 3 types of parser (page 28)
  bs = BeautifulSoup(html.read(), Parser)
  title = bs.body.h1
 except AttributeError as e:
  return None
 return title

url1 = "http://www.pythonscraping.com/pages/page1.html"

title = getTitle(url1)
if title == None:
 print('Title could not be found')
else:
 print(title)
#page 17
url2 = 'http://www.pythonscraping.com/pages/warandpeace.html'#War and peace
html = urlopen(url2)
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
   print(name.get_text())
   # get_text() strips all tags from the document.
   # get_text() should always be the last thing you do, immediately
   #
   #page 18