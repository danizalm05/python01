"""
60_data_analysis_using_Pandas_data_handling.py
 -----------------------------------------------------

https://www.youtube.com/watch?v=H2fL7e6baGw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=61
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial60_data_analysis_using_Pandas_data_handling.py
 

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 
Data handling: Deleting Rows and COlumns
 Deleting columns
 Delete Manual2 column
import pandas as pd
df = pd.read_csv('data/manual_vs_auto.csv')

"""
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/manual_vs_auto_updated.csv')
print(df.head())
print("\ndf.columns = ",df.columns)
 