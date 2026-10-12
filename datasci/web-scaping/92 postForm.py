import requests
from bs4 import BeautifulSoup
'''
we have
first fetch out the form’s HTML source using a GET request,
get the value for the “protection” field, 
and then use that value in the subsequent POST
request. By bringing in Beautiful Soup again.
'''
import requests
from bs4 import BeautifulSoup
url = 'http://www.webscrapingfordatascience.com/postform3/'
# First perform a GET request
r = requests.get(url)
# Get out the value for protection
html_soup = BeautifulSoup(r.text, 'html.parser')
p_val = html_soup.find('input', attrs={'name': 'protection'}).get('value')
# Then use it in a POST request
formdata = {
  'name': 'Seppe',
  'gender': 'M',
  'pizza': 'like',
  'haircolor': 'brown',
  'comments': '',
  'protection': p_val
}
r = requests.post(url, data=formdata)
print(r.text)