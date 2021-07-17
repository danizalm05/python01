"""
 many websites use javascript to populate data.
 To simulate this, I have added the following code to the parsememcparseface page:

<p>Javascript (dynamic data) test:</p>
  <p class='jstest' id='yesnojs'>y u bad tho?</p>
  <script>
     document.getElementById('yesnojs').innerHTML = 'Look at you shinin!';
  </script>

The code basically takes regular paragraph tags, with the class of jstest,
 and initially returns the text"  'y u bad tho?'.
After this, however, there is some javascript defined that will subsequently update
that jstest paragraph data to be 'Look at you shinin!'.
If you open the page in your web browser, we'll see the shinin message,
"""

import bs4 as bs
import urllib.request
u = 'https://pythonprogramming.net/parsememcparseface/'
source = urllib.request.urlopen(u)
#soup = bs.BeautifulSoup(source,'lxml')
soup = bs.BeautifulSoup(source,'html5lib')
js_test = soup.find('p', class_='jstest')

print('\nFull html file'+'\n--------------\n')
print(soup)
print('\njs_test'+'\n--------------\n')
print(js_test)
print('\njs_test.text'+'\n--------------\n')
print(js_test.text)