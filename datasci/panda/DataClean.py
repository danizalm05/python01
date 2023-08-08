#!/usr/bin/env python3
'''

Lesson #5: Data Cleaning - final assignment
Good Movies - The IMDb movie dataset
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/0f960b9a58644ff4b9c375b0624f8d18/b12b949355784e80acfa621095ad6cb8/
https://vproxy.vocareum.com/hostip/172.31.10.40:6000/user/ccc_4d4d451c46_10454_2408356_2408356_537357_0/notebooks/fa05-data-cleaning.ipynb

    Duplicative data  Missing Data  Outliers Data type casting

    
    df.describe()  
    df.hist()
    df.info()
    df.shape
    pd.plotting.scatter_matrix(df)

'''
 
 

import time      # for testing use only
import os         # for testing use only

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

# 1.
# ------------>>>>>>>> load_csv <<<<<<<<------------
 

def load_csv(file_name):
    df = pd.read_csv(file_name)
    return df  

def count_duplicatives(df, col_name=None):
    '''
     Return count of all duplicative rows for the given 'df' parameter 
     dataframe and 'col_name'
    If the 'col_name' parameter is None, you should identify duplicates
    in all columns.

   Note that for a single duplication, all duplicative rows should be 
   counted as duplications,  besides the first one.
   For example, if row a appears 4 times (original + 3) 
   and row b appears 6 times (original + 5),
   we expect to see the result of 8 (3 + 5).
  '''
    if   (col_name == None):
      dup = df.duplicated().sum()
     
    else: 
     dup = df.duplicated(subset=[col_name]).sum()
    
    return dup 




file_name = '.' + os.sep + 'data' + os.sep + 'imdb_movies.csv'

print(file_name)
df_imdb_movies = load_csv(file_name)
print("df_imdb_movies.head()\n--------\n",df_imdb_movies.head())
print("df_imdb_movies.info()\n--------\n",df_imdb_movies.info())
print("df_imdb_movies.shape\n--------\n" ,df_imdb_movies.shape)

dup_rows =  count_duplicatives(df_imdb_movies)
print(" dup_rows = ", dup_rows)
 

dupCount = count_duplicatives( df_imdb_movies)
print ("\nNumber of duplicated items = ",dupCount )

col_name = 'movie_imdb_link'
partial_dup_rows  = count_duplicatives(df_imdb_movies, col_name)
print('partial_dup_rows = ',partial_dup_rows)

'''

'remove_duplicatives'
,
 after removing the duplicatives.
If the 'col_name' parameter is None, you should remove duplicative rows by any 
column
Otherwise, identify and remove duplicates just in regard to the column 'col_name'.
Note that for a each duplication, you should keep only the first occurrence. 

subset: Subset takes a column or list of column label. 
       It’s default value is none. After passing columns,
       it will consider them only for duplicates. 
keep: keep is to control how to consider duplicate value. default is ‘first’. 
    first: considers first value as unique and rest of the same values as duplicate.
    last: it considers last value as unique and rest of the same values as duplicate.
    False: it consider all of the same values as duplicates
inplace: Boolean values, removes rows with duplicates if True.





'''
def remove_duplicatives(df, col_name=None):
 
    df1=df.copy()
    if   (col_name == None):
         df1 = df1.drop_duplicates()
     
    else: 
          df1 = df1.drop_duplicates(subset=[col_name],
                   keep= 'first', inplace=False)
    
    return  df1

    
  

col_name = 'movie_imdb_link'
df_rem_dup_rows =  remove_duplicatives(df_imdb_movies)
df_rem_partial_dups = remove_duplicatives(df_imdb_movies, col_name)
print('Self test; df_rem_dup_rows = ')
print(df_rem_dup_rows)
print('Self test; df_rem_partial_dups = ')
print(df_rem_partial_dups)


def remove_corrupt_rows(df, num_max_missing_cols):
    df1=df.copy()
    df1 = df1.dropna(thresh= num_max_missing_cols, axis=1)
    return df1


file_name = '.' + os.sep + 'data' + os.sep + 'imdb_movies.csv'
col_name = 'movie_imdb_link'
df_imdb_movies = load_csv(file_name)
print("Duplicates in = ", count_duplicatives(df_imdb_movies))
df_cln = remove_duplicatives(df_imdb_movies, col_name)
df_rem_corrupt = remove_corrupt_rows(df_cln, 3)
print("Duplicates out = ", count_duplicatives(df_rem_corrupt))