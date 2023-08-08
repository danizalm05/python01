# -*- coding: utf-8 -*-
"""
Matplotlib Tutorial
https://www.w3schools.com/python/matplotlib_markers.asp
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/59c4963eae864d3f81a006994d06f045/ece47e875cf04aef896799e8ed9ad055/?child=first

"""
 
import pandas as pd
from matplotlib import pyplot as plt
 
import seaborn as sns
 
import warnings
warnings.filterwarnings("ignore") 
 
 
pok = pd.read_csv('data/pokemon.csv', header=0, sep=',') 
 


print("\n\n pok.shape\n------------\n",pok.shape)

'''
A bar plot   of the generation variable devided to normal 
and legendary pokemons. 


  x =  the variable we want to display on the x axis. 
 data = data... 
 kind='count' implies that we would like to present absolute counts, 
 and also that this is going to be a bar plot, 
 hue = the second variable used here, in our case - is_legendary, 
 palette = control the colors used.  

'''


g = sns.catplot(
    x='generation', 
    data=pok,
    kind='count', 
    hue='is_legendary',
    palette=["cyan", "lightcoral"], 
    height=5, 
    aspect=1.5,
    legend=False,
    ).set_axis_labels('Generation', '#of Pokemon')
g.ax.legend(labels=['NON LEGENDARY','LEGENDARY'])

plt.show() 



'''
                 kernel density plots
 ------------------------------
 This graphical representation is for continuous variables, and is somewhat 
 similar to an histogram. However, kernel density plots are based on smoothing 
 the data - thus solving one of the probelsm of histograms.
 Remember that we've said that the number of categories can influence the
 shape of the histogram? 
 On kernel density plots, kernel smoothing is used, and we do not need to 
 specify the number of categories. 

 We will make a kernel density plot for the variable attack, using
 a seabron function. 

'''
sns.kdeplot(pok.attack, shade=True)
plt.show() 


'''
Note that the graph we made describes the distribution of attack,
 a continuous variable. 
 The Y axis does not show the number of observations, but rather a proportion.
 We can see that most of our pokemons have between 50 to 100 attack points. 

We can also make a few such plots on the same graph - thus enabling us to
 compare ditributions.
 For example, let's see both attack and defense together:

'''

ax = sns.kdeplot(pok.attack, shade=True)
sns.kdeplot(pok.defense, shade=True)

plt.show() 