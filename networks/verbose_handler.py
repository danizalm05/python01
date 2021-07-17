#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - verbose_handler.py
# HTTP request handler for urllib2 that prints requests and responses.
#
# customization on the normal HTTP handler. This customization prints out both the
#  outgoing request  and the incoming response instead of keeping them both hidden.
# Example of how to use this file  by other files

# from verbose_http import VerboseHTTPHandler
#  import urllib, urllib2
#  opener = urllib2.build_opener(VerboseHTTPHandler
#  opener.open('http://www.ietf.org/rfc/rfc2616.txt')
import StringIO, httplib, urllib2


class VerboseHTTPResponse(httplib.HTTPResponse):
 def _read_status(self):
    s = self.fp.read()
    print ('-' * 20, 'Response', '-' * 20)
    print (s.split('\r\n\r\n')[0])
    self.fp = StringIO.StringIO(s)
    return httplib.HTTPResponse._read_status(self)

class VerboseHTTPConnection(httplib.HTTPConnection):
    response_class = VerboseHTTPResponse
    def send(self, s):
      print ('-' * 50)
      print (s.strip())
      httplib.HTTPConnection.send(self, s)

class VerboseHTTPHandler(urllib2.HTTPHandler):
  def http_open(self, req):
   return self.do_open(VerboseHTTPConnection, req)