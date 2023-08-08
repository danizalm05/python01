# -*- coding: utf-8 -*-
"""
Scatter plots
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/59c4963eae864d3f81a006994d06f045/9b2de2a90cc64a369291ac4d261d30e4/?child=first
https://www.w3schools.com/python/matplotlib_markers.asp
 
https://courses.campus.gov.il/assets/courseware/v1/45968d0af4d5522948331e6958f6bc25/asset-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1+type@asset+block/L05_NB_Scatter_Line_Pearson.ipynb
"""
 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


pok = pd.read_csv('data/pokemon.csv', header=0, sep=',') 
 
print("\n\n pok.shape\n------------\n",pok.shape)
'''
A scatter plot to examine the relationship between the 
variables defense and attack, using a figure object. 
1. create a figure object.
2. save the object axes  of the new figure into the variable ax. 
3. call scatter using ax with parameters, defense and attack.
3.Add axes labels using xlabel and ylabel.
 '''
 
fig = plt.figure()
ax = plt.axes()
ax.scatter(pok.defense, pok.attack)
plt.xlabel('Defense')
plt.ylabel('Attack')
plt.show()