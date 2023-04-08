'''
BeautifulSoup
Scan Target URL:       https://www.imdb.com/chart/top/

https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/d6d932de573a4e78bcd13d963d42e9a1/c81cb43afa3d4c88b9022d2059e922b5/2?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%408b234a0434e74b09a45c70ea14188d43
https://labs.vocareum.com/main/main.php?m=editor&asnid=537344&stepid=537345&hideNavBar=1


https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=A01N5TZK555GW3553X9G&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1

#load local file from '/data' dir into  beautiful soap.
def load_soup_object(html_file_name):
      myFile=open('./data/'+html_file_name,'r')

      soup=BeautifulSoup(myFile,"html.parser")

      return(soup)
'''

from bs4 import BeautifulSoup
import pandas as pd

import numpy as np
import requests

def load_soup_object(url1):

    user_agent = {'User-agent': 'Mozilla/5.0'}
    response1 = requests.get(url1,headers=user_agent)
    soup = BeautifulSoup(response1.content, "html.parser")
    return(soup)


def scrape_movie_genre_links(html_file_name):

    soup = load_soup_object(html_file_name)
    mtag=soup.find("ul",attrs={"class":"quicklinks"})
    generList =[t['href'] for t in mtag.findAll("a")]

    catg_name =   list()
    catg_html =   list()
    for count,row in enumerate (generList ):
        x1 = row.find("=")
        x2 = row.find("&")
        h = row[x1+1:x2]
        catg_name.append(h.capitalize())
        catg_html.append(h+".html")
    #create the data frame
    d = {'genre_name': catg_name, 'link_to_genre_page':  catg_html}
    df = pd.DataFrame(data=d)

    return df

url ="https://www.imdb.com/chart/top/"

df01 = scrape_movie_genre_links(url)
print(df01)


