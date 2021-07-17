#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 10 - fetch_urllib2.py
# Submitting a form and retrieving a page with urllib2
import mechanize
br = mechanize.Browser()
response = br.open('http://www.weather.gov/')
for form in br.forms():
  print ('%r %r %s' % (form.name, form.attrs.get('id'), form.action))
  for control in form.controls:
    print( ' ', control.type, control.name, repr(control.value))