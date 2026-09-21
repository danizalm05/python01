import requests
from bs4 import BeautifulSoup

url = 'https://linuxsimply.com/linux-basics/os-installation/virtual-machine/kali-linux-on-virtualbox/'
url1 = 'https://news.walla.co.il/item/3868579'
r = requests.get(url)

html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')
first_h3 = html_soup.find('h3')
print("name = ",first_h3.name) # h1
print("content = ", first_h3.contents) # ['List of ', [...],]

print("str()  =  ", str(first_h3))

print("text =", first_h3.text)
 

 