import requests

'''
Apart from the “User-Agent” header, there is another header that deserves 
special mention: the “Referer” header.
 Browsers will include this header to indicate the URL of the web page that
linked to the URL being requested. Some websites will check this to prevent
 “deep links” from working.

'''

url = 'http://www.webscrapingfordatascience.com/referercheck/secret.php'
r = requests.get(url)
print(r.text)
# Shows: Sorry, you seem to come from another web page

'''
When encountering such checks in requests, we can simply spoof the
 “Referer” header as well:
'''

 
my_headers = {
'Referer': 'http://www.webscrapingfordatascience.com/referercheck/'
}
r = requests.get(url, headers=my_headers)
print(r.text)


'''
If you see that requests is not returning the results you expect and have
 observed when using the site in your
browser, inspect the headers through the developer tools to see exactly 

what is going on and duplicate it as well as possible in Python.

'''


