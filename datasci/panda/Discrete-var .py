#!/usr/bin/env python3
'''

https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/59c4963eae864d3f81a006994d06f045/ece47e875cf04aef896799e8ed9ad055/?child=first
Graphical representations for single discrete variables - hence one dimensional
https://matplotlib.org/3.3.3/gallery/index.html

''' 
import pandas as pd
from matplotlib import pyplot as plt

pok = pd.read_csv('data/pokemon.csv', header=0, sep=',') 

print("\n\n pok.shape\n------------\n",pok.shape)



#df.iloc[]: is primarily integer position based (from 0 to length-1 of the axis)
print("\n\n pok.iloc[0])  \n------------\n",pok.iloc[2])
#pie charts
print("\n\n pok['is_legendary'].value_counts()\n------------\n",pok["is_legendary"].value_counts())
pok["is_legendary"].value_counts().plot(kind='pie')
plt.show()
#bar plots
mycolors = ['#002856', '#EAC71B']
pok["is_legendary"].value_counts().plot(kind='bar', color = mycolors)
plt.ylabel('Count')
plt.xlabel('Legendary') 
plt.title('Number of Pokemons')
plt.show()

#Horiz bar plots
pok["generation"].value_counts().plot(kind='barh')
plt.title('Number of Pokemons by generation')
plt.show()

 

print('\n\n\n\n\n\n data/pokemon.csv\n==============\n',pok.head())