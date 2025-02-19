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
 
 15:00
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
fig.tight_layout(pad=3.0)
 #The overlay over histogram is KDE plot (Kernel density distribution)
fig.suptitle("This Main Title is Nicely Formatted", fontsize=16)

axes[0, 0].set_title(' [0,0] Subtitle')
sns.distplot(df['Manual'], ax=axes[0, 0])


axes[0, 1].set_title('[0,1] Subtitle')
sns.distplot(df['Manual'], bins=20, kde=True, rug=True, hist_kws=dict(edgecolor='k', linewidth=0.8),ax=axes[0, 1]) 

axes[0, 2].set_title('kdeplot')
sns.kdeplot(df['Manual'], shade=True,ax=axes[0, 2])

## Add Multiple plots
axes[1, 0].set_title('Auto_th_2 3 4')
sns.kdeplot(df['Auto_th_2'], shade=True,ax=axes[1, 0])
sns.kdeplot(df['Auto_th_3'], shade=True,ax=axes[1, 0])
sns.kdeplot(df['Auto_th_4'], shade=True,ax=axes[1, 0])

axes[1,1].set_title('Simple line')
sns.set(style='darkgrid')   #Adds a grid
sns.lineplot(x='Image', y='Manual', data=df, hue='Unnamed: 0',ax=axes[1, 1])  
 #Simple line plot
#Hue tells seaborn how to color various subcategories, like our set in this example.
axes[1,2].set_title('scatter plot with density curve.')
#Basic scatter plot with density curve.
sns.jointplot(x="Manual", y="Auto_th_2", data=df, kind='reg', color='r')

#KDE plot, Kernel density estimation.
sns.jointplot(x="Manual", y="Auto_th_2", data=df, kind="kde")


#Scatter Plot with linear regression fit. Change order for higher order fits.
sns.lmplot(x='Manual', y='Auto_th_2', data=df, order=1)
#Scatterplot with linear regression fit 
#Separated by hue (e.g. Image_set)
# 95% confidence interval for each set
sns.lmplot(x='Manual', y='Auto_th_2', data=df, hue='Unnamed: 0', order=1)  

 
plt.show()

 


sns.distplot(df['Manual'], bins=20, kde=True, rug=False, hist_kws=dict(edgecolor='y', linewidth=0.8)) 
plt.xlim([80,120])# show values from 80 to 120
plt.show()
sns.kdeplot(df['Manual'], shade=True)

## Add Multiple plots
sns.kdeplot(df['Auto_th_2'], shade=True)
sns.kdeplot(df['Auto_th_3'], shade=True)
sns.kdeplot(df['Auto_th_4'], shade=True)

plt.show()


sns.lineplot(x='Image', y='Manual', data=df, hue='Unnamed: 0')

plt.show()
