# -*- coding: utf-8 -*-


import requests
url1 = 'http://www.webscrapingfordatascience.com/basichttp/'

url2 ='https://www.walla.co.il/'
url3 = 'http://www.webscrapingfordatascience.com/paramhttp/'

r = requests.get(url3)
#Response object containing  information regarding the HTTP reply
 
print(r.text)

# Which HTTP status code did we get back from the server?
print("  r.status_code","\n","--------------")
print(r.status_code)

# What is the textual status code?
print("  r.reason  - textual status code","\n","--------------")
print(r.reason)

# What were the HTTP response headers?
print(" r.headers","\n","--------------")
print(r.headers)

# Request information is a Python object in r.request

print("\n"," r.request","\n","--------------")
print(r.request)

# What were the HTTP request headers?
print("\n","r.request.headers","\n","--------------")
print(r.request.headers)

# The HTTP response content:
print("\n","r.text","\n","--------------")    
print(r.text)