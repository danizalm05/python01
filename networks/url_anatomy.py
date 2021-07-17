#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - url_anatomy.py
# python 2.7
from urlparse import urlparse, urldefrag, parse_qs, parse_qsl

#parse the complex URL to its parts
u = 'http://example.com:8080/Nord%2FLB/logo?shape=square&dpi=96'
p = urlparse(u)
print("URL: %s" % u)

print('Parse URL = ',p) # ParseResult(scheme='http', netloc='example.com:8080',
         #  path='/Nord%2FLB/logo', params='', query='shape=square&dpi=96',
          # fragment='')
print('scheme = ', p.scheme)#Print the scheme parmeter from the result


#page 140
print(parse_qs(p.query))# {'shape': ['square'], 'dpi': ['96']}
print("Query Parmeters:  ")


r = parse_qs('mode=topographic&pin=Boston&pin=San%20Francisco')
print(r)# r is a dictinary

import pprint
pp = pprint.PrettyPrinter(indent=8)
print("Query Parmeters using pprint :  ")
pp.pprint(r)
#Remove the anchor (#),
u = 'http://docs.python.org/library/urlparse.html#item22'
udfrag= urldefrag(u)# the retrun type is a tuple
#('http://docs.python.org/library/urlparse.html', 'urlparse.urldefrag')


print("URL defrag :")


length =len(udfrag)  # Get the number of items in a udfrag Tuple
print("Tuple Length :", length)
print(udfrag)# ('http://docs.python.org/library/urlparse.html','item22'')
print(udfrag[0])  # http://docs.python.org/library/urlparse.html
print(udfrag[1])  # 'item22'

print("slice", udfrag[0:length])
print "this is a tuple: %s" % (udfrag,)# Another way to print a tuple



# Build a URL by calling its geturl() method.
#  When combined with the urlencode() function, which knows how to build
#  query strings, this can be used to construct new URLs:
import urllib, urlparse
query = urllib.urlencode({'company': 'Nord/LB', 'report': 'sales'})
p = urlparse.ParseResult('https', 'example.com', 'data', None, query, None)
url = p.geturl()
print(url)

#Relative URLs
path = 'grants'
url = urlparse.urljoin('http://www.python.org/psf/', path )
print(url)
print "URL + Relative path : %s path= %s " % (url, path)