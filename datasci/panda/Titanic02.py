#!/usr/bin/env python3
'''
                  טיפול בנתונים  כפולים  titanic
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/dd409f280fa04f6b8cb552f715d0a0c4/?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40sequential%2Bblock%40dd409f280fa04f6b8cb552f715d0a0c4
2:44

https://labs.vocareum.com/main/main.php?m=editor&asnid=537350&stepid=537351&hideNavBar=1

2. taking care of data duplication
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/dd409f280fa04f6b8cb552f715d0a0c4/?child=last


'''


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic.csv', header=0, sep=',')
df2 = pd.read_csv('data/titanic_small.csv', header=0, sep=',')
print(" \n====df2 ====\n\n",df2 )
print(" \n====df2.columns====\n")
print(df2.columns,"\n==== end  columns====\n")
print("\n\ndf2.info() \n==============\n\n")
print(df2.info())
print(" \n== end info ====\n\n")

print(" \n== df2.duplicated() ====\n ",df2.duplicated() )
'''
The tree last lines are identical to the first tree lines. so the tree
last values of this out is 'true'
'''
print ("\nNumber of duplicated items = ", df2.duplicated().sum())
print("\n List duplicated items\n----------\n ",df2[df2.duplicated()])
#In the original 'df' there aren't duplicated line so next command is Empty DataFrame
print("\n\ndf[df.duplicated(['Name'])]\n",df[df.duplicated(['Name'])])
print("\n\ndf2[df.duplicated(['Name'])]\n",df2[df2.duplicated(['Name'])])

df3=df2.copy()
print("df3.drop_duplicates()\n---\n",df3.drop_duplicates() )
df3=df2.copy()

#there only 2 possible string for 'Sex' so output of next command will have only 2 lines
print("df3.drop_duplicates(subset=['Sex']) \n-------------\n",df3.drop_duplicates(subset=['Sex']) )
#keep the last duplicate
print("df3.drop_duplicates(subset=['Sex'],keep='last') \n--@@@@@@-\n",
      df3.drop_duplicates(subset=['Sex'],keep='last') )

#delete all duplicate so the  output is an empty table
print("df3.drop_duplicates(subset=['Sex'],keep='false') \n--@@@@@@-\n",
      df3.drop_duplicates(subset=['Sex'],keep=False) )
#https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/dd409f280fa04f6b8cb552f715d0a0c4/?child=last
#What is the number of duplication for Ticket
print(" \n== df2.duplicated() ====\n ",df.duplicated((['Ticket'])).sum() )
#What is the number of unique values for Ticket
count = len(pd.unique(df['Ticket']))
print(" \nnumber of unique values for Ticket =    ",count )
