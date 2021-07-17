import urllib.request
import re

# https://finance.yahoo.com/q?s=AAPL&ql=1
# https://finance.yahoo.com/quote/AAPL?ltr=1
#<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="257">139.34<div></div></span>
# data-reactid="257"

url="http://google.com"
#url="https://finance.yahoo.com/q?s=AAPL&ql=1"
#EXPE
# https://finance.yahoo.com/q?s=EXPE&ql=1
#<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid"http://google.com"="257">121.49<div></div></span>
#data-reactid="257"
# it seems  that   the data-reactid="257"  appears before the closing price
print('Strat loading')
htmlfile = urllib.request.urlopen(url)

htmltext = htmlfile.read()
#print(htmltext[0:100])
        #<h1 class="D(ib) Fz(18px)">Apple Inc. (AAPL)</h1>
#str ='ffffgfbb  <div class="D(ib) Fw(200) Mend(20px)" data-reactid="263"><span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="264">139.71</span><span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($dataGreen)" data-reactid="265">+0.37 (+0.26%)</span><div id="quote-market-notice" class="C($finDarkGray) D(b) Fz(12px) Fw(n) C($finDarkGray)" data-reactid="266"><span data-reactid="267">As of  1:26PM EST. Market open.</span></div></div>'


regex = b'<span>(.+?)</span>'
print(htmltext)
price = re.findall(regex, htmltext)
print(price)
print('End Process')