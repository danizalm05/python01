#!/usr/bin/env python3
'''
      Continuous variables
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/59c4963eae864d3f81a006994d06f045/ece47e875cf04aef896799e8ed9ad055/?child=first
https://matplotlib.org/3.3.3/gallery/index.html
https://datagy.io/matplotlib-title/
Graphical representations for single discrete variables - hence one dimensional

Continuous variables require different graphical representations, since
the number of unique values of each variable may be very large. 
Clearly, pie charts and bar plots won't work well in this case. 

''' 
import pandas as pd
from matplotlib import pyplot as plt

pok = pd.read_csv('data/pokemon.csv', header=0, sep=',') 

print("\n\n pok.shape\n------------\n",pok.shape)

pok.hp.hist(bins=50)
plt.xlabel('Health points')
plt.ylabel('Frequency')
 
plt.title('Freq/Health points  ')
plt.show()
'''
If you   prefer an histogram with relative frequencies - 
 add the parameter *density*, setting its value to True:
'''

pok.hp.hist(density=True)
plt.show()

print('\n\n\n\n\n\n data/pokemon.csv\n==============\n',pok )
pok.speed.hist(bins=50)
plt.xlabel('Speed')
plt.ylabel('Frequency')
plt.title("Speed / Freq ", fontsize='large', loc='left', 
          fontweight='bold', style='italic', family='monospace')

plt.show()
 
##############    Two Histo
fig, ax = plt.subplots(2,3)
fig.tight_layout()

# Adding titles to subplots
ax[0].set_title('Health Points / freq')

plt.subplot(2, 3, 1)
 
pok.hp.hist(bins=10, density=True, rwidth=0.8, color='salmon', grid=False)

plt.xlabel('Health Points')
plt.ylabel('Frequency')
 


plt.subplot(2, 3, 2)
ax[1].set_title(' Speed/ Frequency')
pok.speed.hist(bins=50)
plt.xlabel('Speed')
plt.ylabel('Frequency')

plt.show()
 

ctl = pd.crosstab(pok['generation'], pok['is_legendary'] )
print(ctl)



