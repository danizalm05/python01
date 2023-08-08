# -*- coding: utf-8 -*-
"""
Matplotlib Tutorial
https://www.w3schools.com/python/matplotlib_markers.asp
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/59c4963eae864d3f81a006994d06f045/ece47e875cf04aef896799e8ed9ad055/?child=first

"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
 
 
 
pok = pd.read_csv('data/pokemon.csv', header=0, sep=',') 

print("\n\n pok.shape\n------------\n",pok.shape)

pok.hp.hist(bins=50)
plt.xlabel('Health points')
plt.ylabel('Frequency')
 
plt.title('Freq/Health points  ')
plt.show()


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.xlabel('Health points')
plt.ylabel('Frequency')
pok.hp.hist(bins=50)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)
pok["is_legendary"].value_counts().plot(kind='pie')


plt.subplot(2, 2, 3)
ct1 = pd.crosstab(pok['generation'], pok['is_legendary'],normalize= 'index' )


 

plt.subplot(2, 2, 4)
#ct2 = pd.crosstab(pok['generation'], pok['is_legendary'])
plt.plot(x,y)

plt.show()

print(ct1)  
ct1.plot.bar()
ct1.plot(kind  ="bar", figsize=(5,2))
plt.title('legendary vs normal pokemans', fontsize =14)
plt.ylabel("relative frequcy", fontsize =14)

fig = plt.figure( figsize=(5,2))
fig1 = fig.add_subplot(2,2,1)
fig1.set_title("Attack hist")
fig1.hist(pok.attack,bins=20)

fig2  = fig.add_subplot(2,2,2)
fig2.set_title("defense hist")
fig2.set_xlabel("ffst")
fig2.set_ylabel("1hit")
fig2.hist(pok.defense,bins=20)


fig3  = fig.add_subplot(2,2,3)
fig3.set_title("defgvcst")
fig3.hist(pok.defense,bins=20)


