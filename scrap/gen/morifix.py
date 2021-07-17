from bs4 import BeautifulSoup
import requests

'''
 Can't run in Windows console.
 Windows console font does not support unicode.
'''
#get a translation from English to hebrew
word ='div'
url = 'http://www.morfix.co.il/'+ word
try:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
except Exception as e:
     print('No Internet Connection','\n\n',e)

tr4 = soup.find('div',class_="translation translation_he heTrans")
try:
    out = tr4.text
except Exception as e:
    out  = None  #No p tab
print(out)

tr = soup.find('div',class_="translate_box_en box heWord0")
try:
    out = tr.p.text
except Exception as e:
    out  = None
print(out)

try:
    out = soup.find('div',class_="NoResultsSuggestNewTranslation").text
    print('Word Not Found!')
except Exception as e:
    out  = None  #No p tab