
#http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

import urllib.request
import csv
import sys
from bs4 import BeautifulSoup


prefix= "https://finance.yahoo.com/quote/CSTR?ltr=1"
prefix_bloomberg = "https://www.bloomberg.com/quote/SPX:IND"



#prefix="http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts"

with urllib.request.urlopen(prefix) as url:
     s = url.read()

with urllib.request.urlopen(prefix_bloomberg) as url_bloomberg:
    s_bloomberg = url_bloomberg.read()

soup = BeautifulSoup(s, "html.parser")
soup_bloomberg = BeautifulSoup(s_bloomberg, "html.parser")
#print (soup.prettify())

print("---------------")

#<td class="Ta(end) Fw(b)" data-reactid="331" data-test="PREV_CLOSE-value">19.38</td>
p_yahoo = soup.find('td', attrs={'data-reactid':"331"})
#print (p_yahoo)
#py = p_yahoo.text.strip() # strip() is used to remove starting and trailing
print (p_yahoo)


#print (soup_bloomberg.prettify())
#<div class="price">19.79</div>  <div class="price">19.79</div>
p_bloomberg = soup_bloomberg.find('div', attrs={'class':'price'})
#print(p_bloomberg)
pb = p_bloomberg.text.strip() # strip() is used to remove starting and trailing
print (pb)

#p_bloomberg = soup.find('td', attrs={'data-reactid':"331"})
#share_price = span.text  # strip() is used to remove starting and trailing
#name_box = soup_bloomberg.find('h1', attrs={'class':'name'})
#print (name_box.prettify())

#name = name_box.text.strip() # strip() is used to remove starting and trailing
#print (name)
#price_box = soup.find('div', attrs={'class':'price'})
#price = price_box.text
#print (price)

'''
<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="283">19.38</span>
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

'''