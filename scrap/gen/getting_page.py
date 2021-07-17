import urllib.request
import re
from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
print (type(soup))
#https://www.youtube.com/watch?v=f2h41uEi0xU
# https://finance.yahoo.com/q?s=AAPL&ql=1
# https://finance.yahoo.com/quote/AAPL?ltr=1
#<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="257">139.34<div></div></span>
# data-reactid="257"

urls = ["https://finance.yahoo.com/", "http://www.nytimes.com", "http://www.cnn.com" , "http://google.com"]
regex = b'<title>(.+?)</title>'
pattern = re.compile(regex)
i=0
while i < len(urls):
    print (i+1)
    print("---------------")
    htmlfile = urllib.request(urls[i])
    htmltext = htmlfile.read()
    #htmltext =htmlfile.read()
    title = re.findall(pattern, htmltext)
    print(title)
    print(htmltext[0:100])
    i+=1
   
