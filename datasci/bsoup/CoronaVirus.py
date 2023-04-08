'''
    Crawling  Covid 2019 Data
 https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/d6d932de573a4e78bcd13d963d42e9a1/c81cb43afa3d4c88b9022d2059e922b5/?child=first

 https://labs.vocareum.com/main/main.php?m=editor&asnid=537342&stepid=537343&hideNavBar=1



Scrape data from this wikipedia site about Corona Virus in Israel.
 1.Download the html using requests.
 2.Parse this html with BeautifulSoup.
 3.Extract the html that corresponds to the statistic table with all
      the cities, from the soup.
 4.Parse the "Confirmed COVID-19 cases in Israel by locality with
   population >2,000, tests, and active cases" table into a pandas dataframe. Hint: Both header rows might be harder to parse (as they use row spans). For the purpose of this exercise, exclude all header rows (you can fill it in manually).
 5.Create a table that shows for each city how many cases, new cases,
   and tests they have.
'''


from bs4 import BeautifulSoup
import requests
import pandas as pd

url1="https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Israel"
user_agent = {'User-agent': 'Mozilla/5.0'}
html = requests.get(url1,headers=user_agent)

soup = BeautifulSoup(html.content, "html.parser")

'''
Stage 4 
In the web page look in the botom   for the title:
"Confirmed COVID-19cases in Israel by locality with population>2,000,tests,and active cases" 
and press show. 
so we need tp look for 
"<table class="wikitable sortable mw-collapsible jquery-tablesorter mw-made-collapsible">"
'''

 #Get the first table which contains "wikitable" as class name
tbl =  soup ("table",attrs={"class":"wikitable"})[0]
print("type(tbl) = ",type(tbl))
print("len(tbl) = ",len(tbl))



cities = list()
cases = list()
active_cases = list()
new_cases = list()
test = list()
case_per100 = list()
for count,row in enumerate (tbl("tr")):
    cells = row("td")
    if  ((len(cells)) <6): # 6 celle in a row
        continue
    #print(count," : ",len(cells),cells)
    cities.append(cells[0].get_text().strip())
    cases.append(cells[1].get_text().strip())
    active_cases.append(cells[2].get_text().strip())
    new_cases.append(cells[3].get_text().strip())
    test.append(cells[4].get_text().strip())
    case_per100.append(cells[5].get_text().strip())

d = {'city': cities, 'cases ': cases, 'active_cases': active_cases,
     'new_cases': new_cases, 'test ': test,'  case_per100':  case_per100 }

df = pd.DataFrame(data=d)
print(df)
'''



Python Requests = set of key-value pairs that are sent along with your
 request to a server. They provide information about the request, such 
as the type of request, the data being sent, and the server's response.
 Accept-* headers: the allowed and preferred formats of the response.
 
 
 
Introduction to Web Scraping using Selenium
https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72

https://realpython.com/beautiful-soup-web-scraper-python/
'''

