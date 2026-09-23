import requests
from bs4 import BeautifulSoup

url = 'https://linuxsimply.com/linux-basics/os-installation/virtual-machine/kali-linux-on-virtualbox/'
url1 = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
r = requests.get(url)

html_contents = r.text
 
html_soup = BeautifulSoup(html_contents, 'html.parser')

tag= 'h3'#'h3'

first_tag = html_soup.find(tag)
print("name = ",first_tag.name) 
print("content = ", first_tag.contents) # ['List of ', [...],]

print("str()  =  ", str(first_tag))

print("text =", first_tag.text)
 
print('first_tag.span = ',first_tag.span)
print( '\n id  =',first_tag.span['id']) # firstHeading


print('\n\n------------ h3 ------------')
# Find the first five h3 elements with a   class
tag = html_soup.find_all('h3',  limit=2)
 
print(tag)
 

'''
<h3><span class="ez-toc-section" id="Step_2_Create_a_New_Virtual_Machine" ez-toc-data-id="#Step_2_Create_a_New_Virtual_Machine"></span>Step 2: Create a New Virtual Machine<span class="ez-toc-section-end"></span></h3>
'''