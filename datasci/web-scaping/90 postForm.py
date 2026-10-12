import requests
from bs4 import BeautifulSoup
'''
  
'''

import requests
url = 'http://www.webscrapingfordatascience.com/postform3/'
# No GET request needed?
formdata = {
   'name': 'Seppe',
   'gender': 'M',
   'pizza': 'like',
   'haircolor': 'brown',
   'comments': '',
   'protection': 'a90d3cd57e912cc3f57790d98587c7e1'
}
r = requests.post(url, data=formdata)
print(r.text)
# Will show: Are you trying to submit information from somewhere else?