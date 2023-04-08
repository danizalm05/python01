'''
BeautifulSoup
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/d6d932de573a4e78bcd13d963d42e9a1/a14dc30dd5a04124b57b7bf8df3516ac/?child=first
https://labs.vocareum.com/main/main.php?m=editor&asnid=537338&stepid=537339&hideNavBar=1
'''


from bs4 import BeautifulSoup

# we tell BeautifulSoup and tell it which parser to use
song_soup = BeautifulSoup(open("./lyrics.html"), "html.parser")
print(type(song_soup))
print(song_soup.prettify())
print(song_soup.title )
print(song_soup.title.string)
print(song_soup.div.string)#Print content of first div
print("      -----id=zep------\n",song_soup.find(id="zep"))# find a specific element
text = song_soup.find(id="zep").get_text() # get only text
print(text)


h1s = song_soup.find_all("h1")# get all instances of a tag:
print(h1s)
string_h1s = [tag.get_text() for tag in h1s]#get the text
print(string_h1s)
#you can use a shortcut by just calling directly on an object:
print(song_soup("div"))
