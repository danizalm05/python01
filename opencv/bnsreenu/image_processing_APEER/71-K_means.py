"""
71-K_means.py
71a-K_means_demo.py

 -------------------------------------------
https://www.youtube.com/watch?v=H_L7V_BH9pc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=73

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial71-K_means.py
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial71a-K_means_demo.py
data file url
 
"""


import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_excel('data/K_Means.xlsx')
print(df.head())

import seaborn as sns
sns.regplot(x=df['X'], y=df['Y'], fit_reg=False) 
plt.show()