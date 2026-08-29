# -*- coding: utf-8 -*-
import requests
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
r = requests.get(url)
print(r.text)
# Will show: I don't have any information on "test"