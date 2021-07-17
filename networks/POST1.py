#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 -
# Demonstrating the POST action (parameters are send by form)
#Example
#   <form name="myloginform" action="/access/dummy" method="post">
#      E-mail: <input type="text" name="e-mail" size="20">
#      Password: <input type="password" name="password" size="20">
#     <input type="submit" name="submit" value="Login">
# </form>

'''
The HEAD Method
It’s possible that you might want your program to check a series of links for validity or whether they have
moved, but you do not want to incur the expense of actually downloading the body that would follow the
HTTP headers. In this case, you can issue a HEAD request. This is directly possible through httplib, but it
can also be performed by urllib2 if you are willing to write a small request class of your own:
'''


class HeadRequest(urllib2.Request):
 def get_method(self):
    return 'HEAD'








from verbose_handler import VerboseHTTPHandler
# using the 'verbose_handler.py' to prints requests and responses.
import urllib, urllib2


info = urllib2.urlopen(HeadRequest('http://www.google.com/'))
header = info.read()
print (header)


opener = urllib2.build_opener(VerboseHTTPHandler)
url = 'http://forecast.weather.gov/zipcity.php'
form = urllib.urlencode({'inputstring': 'New York, NY'})#  form values
#page 149
try:
    info = opener.open(url, form)
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

keys = sorted(info.headers.keys())# key is alist of key headers

print (keys)

print("File contant")

#bring the entire data stream into memory as a single string:
print (info.read().strip())

#you can also  read the info object in pieces through read(N)
#  or readline();
#line  147