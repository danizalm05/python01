import requests
from bs4 import BeautifulSoup
url = 'https://news.walla.co.il/item/3868579'
r = requests.get(url)
html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')
# Find the first h1 tag
first_h1 = html_soup.find('h1')


if first_h1:
    print(first_h1.name)
    print(first_h1.contents)
else:
    print("לא נמצאה תגית h1")

print(first_h1.contents)    