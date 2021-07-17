#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 -
# Demonstrating the POST action (parameters are send by form)



# The HEAD Method
# # moved, but you do not want to incur the expense of actually downloading the body that would follow the
# HTTP headers. In this case, you can issue a HEAD request. This is directly possible through httplib, but it
# can also be performed by urllib2 if you are willing to write a small request class of your own:
#

from verbose_handler import VerboseHTTPHandler
# using the 'verbose_handler.py' to prints requests and responses.
import urllib, urllib2


class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'




# page 149
try:
    info = urllib2.urlopen(HeadRequest('http://www.google.com/'))
    header = info.read()
    print("Message")
    print(info.code,'  ',info.msg)

    print("headers")
    print(info.headers)
except urllib2.HTTPError, e:
    error_code = e.code
    print("Error Code = '%s'." % error_code)
    error_msg = e.msg
    print("Error msg = '%s'." % error_msg)
    print("Error File content")

    # bring the entire data stream into memory as a single string:
    print (e.read().strip())

# line  147