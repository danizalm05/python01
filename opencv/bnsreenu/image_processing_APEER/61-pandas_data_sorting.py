"""
61_data_analysis_using_Pandas_data_sorting.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=Kn_Gl12GWq0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=62
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial61_data_analysis_using_Pandas_data_sorting.py
data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 

"""    
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/manual_vs_auto_updated.csv')
print(df.head())
print("\n\n\ndf.columns = ",df.columns)
