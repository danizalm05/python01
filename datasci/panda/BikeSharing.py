#!/usr/bin/env python3
'''
                   מבוא למדעי הנתונים: כלים ושיטות
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/77fc2aaac3df441d8fb1de017676dacf/20d8dee887434b6ca29c4970cb23924a/1?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%405758ab9fdb454a8bb403aa34c933ee67
https://labs.vocareum.com/main/main.php?m=editor&asnid=537346&stepid=537347&hideNavBar=1
'''


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


df = pd.read_csv('./data/day.csv', header=0, sep=',')
print(df.head())
print(df.info(),df.shape)
#The distribution   using 'value_counts' : occurrences of unique values in Series
# 21 holiday 710 regular days total 731 days
dist = df['holiday'].value_counts()
print('distribution of  holiday = ',dist)
#Setting the parameter 'normalized' to True
distNormal = df['holiday'].value_counts(normalize=True)
print('Normalize distribution of  holiday = ', distNormal)
fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(331)
ax1.set(title='distribution of  holidays', xlabel='holiday #', ylabel='# day')
ax1  =df['holiday'].value_counts().plot(kind='pie' )

ax2 = fig.add_subplot(332)
ax2.set(title='distribution of  holidays', xlabel='holiday #', ylabel='# day')
mycolors = ['#002856', '#EAC71B']
ax2 = df['holiday'].value_counts().plot(kind='bar', color=mycolors)

ax3 = fig.add_subplot(333)
ax3.set(title='5 bin of temp', xlabel='temp #', ylabel='# day')
plt.hist(df["temp"],bins=5)


ax4 = fig.add_subplot(334)
ax4.set(title='10 bin of temp', xlabel='temp #', ylabel='# day')
plt.hist(df["temp"],bins=10)







#With a continuous variable, we can create bins using panda's cut command :


binNorm = pd.cut(df["temp"],bins=5).value_counts(normalize=True)
print('binNorm\n', binNorm, '\n')

#In historgram plots we devide variable's values to bins, and then plot them :
bin= pd.cut(df["temp"],bins=5).value_counts()
print('bin\n',bin,'\n')




# The decscribe command also gives us important statistics such as mean, std, min & max

print(df.cnt.describe())
#For checking the likelihood of certain scenarios or events, we can use the count command,
# combined  with a logical condition :
likelihood = df.cnt[df.cnt > 5000].count()
print('df.cnt[df.cnt > 5000].count()  =  ',likelihood)

print("probability for cnt[df.cnt > 5000]  = ",df.cnt[df.cnt > 5000].count()/df.cnt.count())
df.cnt.describe()


ax5 = fig.add_subplot(335)
ax5.set(title='registered cnt ', xlabel='df.registered#', ylabel='# df.cnt')
plt.scatter(df.registered, df.cnt)



plt.show()

mean = df["temp"].mean()
print("mean = ",mean )
df.cnt.std()
print("df.cnt.std() = ",df.cnt.std())