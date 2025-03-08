"""
64-basic_plotting_of_data_from_pandas_dataframe.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=Idzm6qlMEiw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=65
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial64_basic_plotting_of_data_from_pandas_dataframe.py

data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 7:00

"""    
 
import pandas as pd
import matplotlib.pyplot as plt 

csv_name = 'data/manual_vs_auto_updated.csv'

df = pd.read_csv(csv_name)
print("\n    ", csv_name,"\n    ==============================")
print(df.head())

#Pandas works with Matplotlib in the background. SO we don't
# have to import Pyplot for basic plotting.

#To plot single histogram based on single value
#df['Manual'].plot(kind='hist', title='Manual Count')
df['Manual'].plot(kind='hist', title='Manual Count', bins=30, figsize=(12,10)) #Can also add bins and fig size
plt.show()

#To work only with Set 1 data we can create a new 
#dataframe for that specific set
#and work with that dataframe. 
#Let us plot only Set 1.

#Change Unnamed: 0 name to Image_set
df = df.rename(columns = {'Unnamed: 0':'Image_set'})
print("df.columns \n=========\n",df.columns) 
set1list = df['Image_set'] == 'Set1'
set1_df = df[set1list]
set1_df['Manual'].plot()
plt.show()


# Sometimes you need to smooth data for better visualization.
#One way to Smooth is by averaging few points 
df['Manual'].rolling(3).mean().plot()  #MUch nicer plot.
#Can do rolling mean or sum or anything else that makes sense.
#Some disconnects, let's not worry about it for now.
plt.show()


print(df['Manual'].describe())
#This can be graphically represented using box plot.
df['Manual'].plot(kind="box", figsize=(8,6))  #Shows max and min values, outliers, etc.
plt.show()

#In order to plot the relationship between Columns, we typically generate scatter 
#plots

df.plot(kind='scatter', x='Manual', y='Auto_th_2', title='Manual vs Auto2')
plt.show()
#### Using functions and creating Caterogries and plotting

#Now, Let's go through an exercise where we define all cell counts
# below 100 as low  and above as high.
# Then let's plot using the new categories we defined.

# define a function to categorize low and high counts.
def cell_count(x):
    if x <= 100.0:
        return "low"
    else:
        return "high"

#Now we want to send the entire Manual column through this function, which is what apply() does:
#Start by defining a new column title cell_count_index
#Then just apply the function to categorize counts into low and high.
df["cell_count_index"] = df["Manual"].apply(cell_count)
print(df.head())
#Creates a new column called grain_category
#Can save to new csv
#df.to_csv('data/manual_vs_auto2.csv')

print(df.loc[20:30, ['Manual', 'cell_count_index']]) #Verify 20-30 rows.

#we can plot by combining this cell count index information
df.boxplot(column='Manual', by='cell_count_index')

plt.show()