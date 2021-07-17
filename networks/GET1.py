#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 -
# using the 'verbose_handler.py' to prints requests and responses.
# url = 'http://example.com/better-living-through-http'
url ='http://www.bbc.com'
from verbose_handler import VerboseHTTPHandler
import urllib, urllib2
opener = urllib2.build_opener(VerboseHTTPHandler)
#info = opener.open(url)# open and print verbose massages
#In case the URL does not exist the header of 404 message is printed
# and after this header a python error message and Exit 1

try:
    info = opener.open(url)
except urllib2.HTTPError, e:
    error_code = e.code
    print("Error Code = '%s'." % error_code)
    error_msg = e.msg
    print("Error msg = '%s'." % error_msg)
    print("Error File content")

    # bring the entire data stream into memory as a single string:
    print (e.read().strip())

code = info.code
print("Code = '%s'." % code)
msg = info.msg
print("msg = '%s'." % msg)
#page 143
keys = sorted(info.headers.keys())# key is alist of key headers

print (keys)

print("File contant")

#bring the entire data stream into memory as a single string:
print (info.read().strip())

#you can also  read the info object in pieces through read(N)
#  or readline();
#line  147