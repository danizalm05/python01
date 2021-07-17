#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

import urllib.request
import csv
import sys
from bs4 import BeautifulSoup


prefix= "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
#prefix="http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts"
with urllib.request.urlopen(prefix) as url:
    s = url.read()

soup = BeautifulSoup(s, "html.parser")


print("---------------")
table = soup.find('tbody', attrs={'class': 'stripe'})
#print (table.prettify())
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):

        text =cell.text.replace('&nbsp;', '')#erase  &nbsp
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
print (list_of_rows)

if sys.version_info >= (3,0,0):
    outfile = open("./inmates.csv", "w",newline='')
else:
    outfile = open("./inmates.csv", "wb")



writer = csv.writer(outfile)
writer.writerows(list_of_rows)