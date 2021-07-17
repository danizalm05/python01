#  https://www.youtube.com/watch?v=qgDBLD7EChI&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=5
# Web Scraping with Python: Collecting Data from the Modern Web - O'Reilly Media
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())