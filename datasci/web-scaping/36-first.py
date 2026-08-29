# -*- coding: utf-8 -*-


import requests
url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)
#Response object containing  information regarding the HTTP reply
 
print(r.text)