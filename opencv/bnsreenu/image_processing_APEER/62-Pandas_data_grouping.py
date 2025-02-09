"""
62 Pandas_data_grouping.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=4l4xQ6Ln_5o&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=63
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial62_data_analysis_using_Pandas_data_grouping.py
#Using group by 
#Group-by’s can be used to build groups of rows based off a 
specific feature 
eg. the Set name in our csv dataset, we can group by set 1, 2, 3,
 and 4
We can then perform an operation such as mean, min, max, std on 
the individual groups    

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
"""    
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/manual_vs_auto_updated.csv')

# rename Unnamed column and drop Manual 2 column
df = df.rename(columns = {'Unnamed: 0':'Image_set'})
df = df.drop("Manual2", axis=1)
print(df.head())

group_by_file = df.groupby(by=['Image_set'])
set_data_count = group_by_file.count()  #Count for each value per group
set_data_avg = group_by_file.mean(numeric_only=True)   #Mean for each value per group
print("\nset_data_count\n -----------\n",set_data_count)
print("\nset_data_avg\n -----------\n",set_data_avg)

group_by_file_count = df.groupby(by=['Image_set']).count()
group_by_file_mean  = df.groupby(by=['Image_set']).mean(numeric_only=True) 
group_by_file_sum  = df.groupby(by=['Image_set']).sum() 

 


#Correlation between data


