#https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
print (soup.prettify())#.encode('utf8'))
match = soup.title.text
print('Title =',match)
 
#header = soup.find_all('header',class_='entry-header')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None  # The video link is missing

    print(yt_link)

print()

#39:50
# https://www.youtube.com/watch?v=ng2o98k983k