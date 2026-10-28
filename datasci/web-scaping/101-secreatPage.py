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



print('\nhttp://www.webscrapingfordatascience.com/redirect/')
url = 'http://www.webscrapingfordatascience.com/redirect/'
r = requests.get(url)
print(r.text)
print(r.headers)


'''
For the aove URL,two requests are being made by
your browser: the first to the original URL, which now returns a 302 status code. This
status code instructs your browser to perform a second request to the “destination.php”
URL.

Note that we get the HTTP reply corresponding with the final destination (“you’ve
been redirected here from another page!”).


'''
'''
if we want to see the contents of the “Location” and
“SECRET-CODE” headers manually? To do so, you can simply turn off requests
 default:
      r = requests.get(url, allow_redirects=False)
behavior of the following redirects through the allow_redirects argument:
 
'''

print('\n\n  allow_redirects=False')
 
url = 'http://www.webscrapingfordatascience.com/redirect/'
r = requests.get(url, allow_redirects=False)
print(r.text)
print(r.headers)