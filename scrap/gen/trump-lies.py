<<<<<<< HEAD
import requests
import pandas as pd
from bs4 import BeautifulSoup
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))


df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
print(df)
=======
import requests
import pandas as pd
from bs4 import BeautifulSoup
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))


df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
print(df)
>>>>>>> c2d771f50ca5f8c82993c45f679a270a5196ad6a
#df.to_csv('trump_lies.csv', index=False, encoding='utf-8')