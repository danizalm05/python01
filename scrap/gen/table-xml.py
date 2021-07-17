 #https://www.youtube.com/watch?v=sAuGH1Kto2I&index=3&list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS

import bs4 as bs
import urllib.request
import pandas as pd
u1 = 'https://pythonprogramming.net/parsememcparseface/'
u  = 'http://www.the-athenaeum.org/'
source = urllib.request.urlopen(u1).read()
soup = bs.BeautifulSoup(source,'html5lib')

#This page just has one table, so we can get away with doing:

table = soup.table   #OR we could do:  table = soup.find('table')
print('\n\n rows within the table'+'\n--------------\n')

#Next, we can find the table rows within the table:
table_rows = table.find_all('tr')

#iterate through the rows, find the td tags, and then print out each of the table data tags:
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
#The first row is empty, since it has table header (th) tags, not table data (td) tags



source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()

soupx = bs.BeautifulSoup(source, 'html5lib')
print(soupx)


#grab the urls:
print('grab the urls \n')
for url in soupx.find_all('loc'):
    print(url.text)


#dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
#for df in dfs:
#    print(df)