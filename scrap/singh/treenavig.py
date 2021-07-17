# Web Scraping with Python: Collecting Data from the Modern Web - O'Reilly Media
# page  26
# https://www.youtube.com/watch?v=GC890_Rco3g&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=7
# Beautiful Soup Documentation :
#     https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from urllib.request import urlopen
from bs4 import BeautifulSoup
url1 = "http://www.haarchion.co.il/poet/%d7%a9%d7%9c%d7%9e%d7%94-%d7%90%d7%91%d7%9f-%d7%92%d7%91%d7%99%d7%a8%d7%95%d7%9c/"
url2 = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url1)

bsObj = BeautifulSoup(html, "lxml")
#  <table id="giftList">
#for child in bsObj.find("table", {"id": "giftList"}).children:


print("child in bsObj.find")
for child in bsObj.find("table", {"class": "playlist"}).children:
    print(child)
print("sibling in bsObj.find")

