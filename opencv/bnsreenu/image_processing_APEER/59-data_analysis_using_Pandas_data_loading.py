"""
59 data_analysis_using_Pandas_Intro_data_loading.py
 -----------------------------------------------------

https://www.youtube.com/watch?v=qy5b2RCdW9o&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=60
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial59_data_analysis_using_Pandas_Intro_data_loading.py  

Think of Pandas as an extension of Numpy where it makes handling of arrays
easy, almost like Excel.


data file url
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cell_measurements.csv
 
12:00
"""
 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('data/cell_measurements.csv')
print(df.head())
print(df.columns)
df['Area'].plot(kind='hist', title='Area', bins=50)
#df.plot(x='Year', y='Unemployment Rate', kind='line')
plt.show()

#Now let us pass data directly.
'''
data = [[10, 200, 60],
        [12, 155, 45],
        [9, 50, -45.],
        [16, 240, 90]] 
         
#df = pd.DataFrame(data, index = [1,2,3,4], columns = ['Area', 'Intensity', 'Orientation'])
#print(df)
'''

###########################################
#Now let us load data from a text or csv file
#Dataset showing Different image sets (25 images in each set)
#Total 100 images analyzed manually and automatically using cell counting algorithm
#Each image was manually analyzed to count cells
#An attempt was made to count manually by a different person but gave up 
#Then analyzed using the algorithm we developed earlier, 
#by changing a parameter 3 times, giving different cell counts each time 


df = pd.read_csv('data/manual_vs_auto_updated.csv')
print(" \n\n         =====   info      =====\n")
print(df.info())  #Prvides an overview of the dataframe. 
print("\n\nshape = ", df.shape,"\n\n")#How many rows and columns

print(" \n\n         =====  Shows a lot of stuff but truncated =====\n") 
print(df)  #Shows a lot of stuff but 
print(" \n\n         =====  df.head(7) =====\n") 
print(df.head(7))  #Default prints 5 rows from the top
#First default column you see are indices. 
print(" \n\n         ===== df.tail() =====\n") 
print(df.tail())   #Default prints 5 rows from the bottom

#First line in csv is considered header, even if you don't specify
#First column is the index and it goes from 0, 1, 2, ....
#Index is not part of the data frame
#INdex is the unique identifier of a row, in our case a specific grain in a specific image
#Any of the other columns can be assigned as index if we know it is a unique identifier. 
 
print(df.index)  #Defines start and stop with step size. Not very exciting with default index
print("\ndf.index = ",df.index,"\n")#How many rows and columns
#But can be useful if we assign other column as index. 
df = df.set_index('Image')
print(" \n\n         ===== after df.set_index('Image') =====\n") 
print(df.head())
#View all column names.
print("\ndf.columns = ",df.columns) #Image name column disappeared as it is used as index. 

#TO look at all unique entires. In this case, our 3 file names. 
print("unique() = ",df['Unnamed: 0'].unique())  

#If unnamed is bothering you then you can change the name.
df = df.rename(columns = {'Unnamed: 0':'Image_set'})
print("\n\n change -unnamed- to image set :\n",df.columns) 


#Missing data is encoded as NaN so we can work with them in a friendly
# manner. 
#Let us look at Manual column to see what it has.
print("\ndf[Manua]", df["Manual"])  #Shows NAN. We can fill it with something or ignore it or remove the column
#Let us look at manipulating data in our next video. 

#For now let us finish by looking at a couple more useful functions. 
#Pandas automatically recognizes correct data types.

print("\ndf.dtypes\n",df.dtypes)  



"""

#Similarly multiple column names can be changed at once. 
df = df.rename(columns = {'equivalent_diameter':'Diameter(um)', 
                          'Area':'Area(sq. um)',
                          'orientation':'orientation (deg)',
                          'MajorAxisLength':'Length (um)',
                          'MinorAxisLength':'Width (um)',
                          'Perimeter':'Perimeter (um)'})
print(df.dtypes)
"""

print("\ndf.describe()\n",df.describe())  #Gives statistical summary of each column. 