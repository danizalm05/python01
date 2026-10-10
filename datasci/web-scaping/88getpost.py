import requests
from bs4 import BeautifulSoup
'''
  
'''

url = 'http://www.webscrapingfordatascience.com/postform2/'
# First perform a GET request
r = requests.get(url)
print(r.text) 

# Followed by a POST request
formdata = {
 'name': 'Seppe',
 'gender': 'M',
 'pizza': 'like',
 'haircolor': 'brown',
'comments': ''
}
r = requests.post(url, data=formdata)
print(r.text)