"""
65_pandas_data_plotting_using_Seaborn.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=jcMQAXy2cVo&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=67
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial65_pandas_data_plotting_using_Seaborn.py

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv


#Seaborn builds on top of matplotlib to provide a richer out of 
the box environment. 
 https://seaborn.pydata.org/
https://seaborn.pydata.org/examples/index.html   
 pip install seaborn
 
 7:00
"""    
 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
csv_name = 'data/manual_vs_auto_updated.csv'

df = pd.read_csv(csv_name)
print("\n    ", csv_name,"\n    ==============================")
print(df.head())
##############
#Single variable (distribution histogram plots)
#sns.distplot(df['Manual'])  #Will fail as we have a few missing values.
 
print("\n df.isnull().sum() )\n================\n",df.isnull().sum() )#Most useful. Tells us where we have null values.
df = df.drop(['Manual2'], axis=1)
#Let us fill missing values with a value of 100
df['Manual'].fillna(100, inplace=True)
##################################################### 

#Distribution plot (Histogram)
#sns.distplot(df['Manual'])   #The overlay over histogram is KDE plot (Kernel density distribution)

#Making it visually appealing
#sns.distplot(df['Manual'], bins=20, kde=True, rug=False, hist_kws=dict(edgecolor='k', linewidth=0.8)) 
#plt.show()



#============================   Output  ===============================   

fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 8))
 #The overlay over histogram is KDE plot (Kernel density distribution)
sns.distplot(df['Manual'], ax=axes[0, 0])
#Making it visually appealing
sns.distplot(df['Manual'], bins=20, kde=True, rug=False, hist_kws=dict(edgecolor='k', linewidth=0.8),ax=axes[0, 1]) 


plt.show()

 


plt.xlim([80,120])# show values from 80 to 120
sns.distplot(df['Manual'], bins=20, kde=True, rug=False, hist_kws=dict(edgecolor='y', linewidth=0.8),ax=axes[0, 2]) 
plt.show()
'''

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(4,3,1)
ax1.title.set_text('.distplot(df[Manual]')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(4,3,2)
ax2.sns.distplot(df['Manual']) 
ax2.title.set_text('.distplot(df[Manual]')

ax3 = fig.add_subplot(4,3,3)
ax3.sns.distplot(df['Manual'], bins=20, kde=True, rug=False, hist_kws=dict(edgecolor='k', linewidth=0.8)) 
ax3.title.set_text('hist color range')

ax4 = fig.add_subplot(4,3,4)
#ax4.imshow(thresh, cmap='gray')
ax4.title.set_text('thresh')


ax5 = fig.add_subplot(4,3,5)
#ax5.imshow(opening1)#,cmap='gray')
ax5.title.set_text('opening1')



ax6 = fig.add_subplot(4,3,6)
#ax6.imshow(opening2)#, cmap='gray')
ax6.title.set_text('opening2')

ax7 = fig.add_subplot(4,3,7)
#ax7.imshow(sure_bg, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(4,3,8)
#ax8.imshow( sure_fg , cmap='gray')
ax8.title.set_text(' sure_fg ')


ax9 = fig.add_subplot(4,3,9)
#ax9.imshow(unknown, cmap='gray')
ax9.title.set_text('unknown')

#
ax10 = fig.add_subplot(4,3,10)
#ax10.imshow(markers)#, cmap='gray')
ax10.title.set_text('markers')

 

ax11 = fig.add_subplot(4,3,11)
#ax11.imshow(markers10,cmap='gray')
ax11.title.set_text('markers10')
'''
 


