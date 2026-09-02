# -*- coding: utf-8 -*-
import requests
url01 = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
url02 = 'http://www.webscrapingfordatascience.com/paramhttp/?query=a queryv with spaces'

r = requests.get(url02)

# Will show: I don't have any information on "test"


# Parameter will be encoded as 'a%20query%20with%20spaces'
# You can verify this be looking at the prepared request URL:
print(r.request.url)
print(r.text)
url00 = 'http://www.webscrapingfordatascience.com/paramhttp/'
parameters = {
'query': 'a query with /, spaces and?&'
}
r = requests.get(url00, params=parameters)
print(r.url)
print(r.text)



def calc(a, b, op):
 url = 'http://www.webscrapingfordatascience.com/calchttp/'
 params = {'a': a, 'b': b, 'op': op}
 r = requests.get(url, params=params)
 return r.text
print(calc(4, 6, '*'))
print(calc(4, 6, '/'))