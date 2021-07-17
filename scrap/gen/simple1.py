import bs4 as bs
import urllib.request
#https://www.youtube.com/watch?v=aIPqt-OdmS0&list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS
#lxml in c:\users\normi\anaconda3\lib\site-packages
#http://www.the-athenaeum.org/art/counts.php?s=au&m=a

u1 = 'https://pythonprogramming.net/parsememcparseface/'
u  = 'http://www.the-athenaeum.org/'
#ecj_data = open("art.htm",'r').read()

#soup = BeautifulSoup(ecj_data)
source = urllib.request.urlopen(u1).read()
#"html.parser"
soup = bs.BeautifulSoup(source, "html.parser")#HTTP Error 403: Forbidden for 'u'
#soup = bs.BeautifulSoup(source, "html5lib" )
#soup = BeautifulSoup(html, "html5lib")
# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

print('find_all( p ) = ',soup.find_all('p'))
# getting specific values:
#print(soup.find_all('p'))
for paragraph in soup.find_all('p'):  # print only the text
    #print('string=',paragraph.string)# produces a NavigableString object there are child nodes
    print(str(paragraph.text))#text is just typical unicode text . this  is more common

#Grab links
print('href'+'\n')
for url in soup.find_all('a'):
    print(url.get('href'))

#we can specify a new Beautiful Soup object. An example might be:

nav = soup.nav

#Next, we can grab the links from just the nav bar:
print('\n\n url in nav.find_al'+'\n--------------\n')
for url in nav.find_all('a'):
    print(url.get('href'))

#To get the body section, then grab the .text from there:
body = soup.body
print('\n\n body.find_all'+'\n--------------\n')
for paragraph in body.find_all('p'):
    print(paragraph.text)

# multiple tags with the same names, but different classes,
#Note the class_='body', which allows us to work with a specific class of tag.
for div in soup.find_all('div', class_='body'):
    print(div.text)
