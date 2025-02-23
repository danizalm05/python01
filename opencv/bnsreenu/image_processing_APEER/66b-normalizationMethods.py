"""
66b-Applying various normalization methods in python
 ------------------------------------------- 
https://www.youtube.com/watch?v=0Vly0hajtLo&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=68
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial66b_various_data_normalization_techniques.py
"""
import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
 
#import 'housing into aata  frame
df = pd.DataFrame(data= np.c_[housing['data'], housing['target']],
                     columns= housing['feature_names'] + ['target'])

#df = pd.read_csv("data/normalization.csv")
print("\ndf.describe().T\n===========\n")
print(df.describe().T)

#
#Define the dependent variable that
# needs to be predicted (labels) .
#the target column is the price of the house
Y = df["target"].values


#Define the independent variables.
# ,so we can normalize other data
X = df.drop(labels = ["target"], axis=1) 