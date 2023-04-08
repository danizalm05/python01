'''
BeautifulSoup
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/d6d932de573a4e78bcd13d963d42e9a1/3ba36134f4204cd5bad34ba6968d875b/?child=first
https://labs.vocareum.com/main/main.php?m=editor&asnid=537340&stepid=537341&hideNavBar=1
hhttps://www.rd.com/jokes/

#load local file from '/data' dir into  beautiful soap.
def load_soup_object(html_file_name):
      myFile=open('./data/'+html_file_name,'r')

      soup=BeautifulSoup(myFile,"html.parser")

      return(soup)
'''

from bs4 import BeautifulSoup
import requests

url1="https://www.rd.com/jokes/"
user_agent = {'User-agent': 'Mozilla/5.0'}
response1 = requests.get(url1,headers=user_agent)
soup1 = BeautifulSoup(response1.content, "html.parser")
#print(soup1)

mtag=soup1.find("div",attrs={"class":"joke-tax-popular"})

linksToPages=[t['href'] for t in mtag.findAll("a")]#Creat a list of URL
print(linksToPages)

import requests
#urls=linksToPages
urls=['https://www.rd.com/jokes/animal/','https://www.rd.com/jokes/animal-puns/']
for url2 in urls:
    response1 = requests.get(url2,headers=user_agent)
    soup1 = BeautifulSoup(response1.content)
    for t in soup1.findAll("div",attrs={"class":"content-wrapper"}):
        print(t.text)
        print("####################")
'''
Python Requests = set of key-value pairs that are sent along with your
 request to a server. They provide information about the request, such 
as the type of request, the data being sent, and the server's response.
 Accept-* headers: the allowed and preferred formats of the response.
 
 
 
Introduction to Web Scraping using Selenium
https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72

https://realpython.com/beautiful-soup-web-scraper-python/
'''