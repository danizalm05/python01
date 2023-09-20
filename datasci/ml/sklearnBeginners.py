#!/usr/bin/env python3
'''
Introduction to sklearn and ML Data Pre-processing

https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/6c93ec048fa047efbef02828a32bb0d0/b37f098fbe18488e865593740c38e5ea/6?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%40c1c7dff808d84413b7d1c0825b63e588
https://labs.vocareum.com/main/main.php?m=editor&asnid=537360&stepid=537361&hideNavBar=1

https://scikit-learn.org/stable/tutorial/basic/tutorial.html
https://scikit-learn.org/stable/
https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/

dataset: Womens Clothing E-Commerce Reviews
For each review, we have 3 parts of information:
1.Product information , 2. Review data , 3.Reviewer data
'''

import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression

#
df = pd.read_csv("./data/ClothingReviews.csv")
print('\n\n')
print("Head of ClothingReviews.csv\n-------------------------\n\n ")
print(df.head())
'''
StandardScaler: maps the values into the  standrad distribution 
(mean=0 std=1)
we will apply it on all numeric values. 
You can see that even the StandardScaler uses the fit and transform 
methods.
fit learns the values in order to normalize and transform applies it. 
In order to learn it and then apply it directly on the train set, 
you can  use the fit_transform method

Scaling is also trained on the train set, and then applied to the test set. 
We do not scale the entire data set at once (we always do train first and 
then apply it on test)


'''

'''
Our goal is to build a supervised machine learning model to predict 
whether a given user is recommending a product or not. 
For simplicity reasons we will  create a copy dataframe only with
 numeric data:
'''
df_copy=df[["Clothing ID","Age","Rating","Recommended IND","Positive Feedback Count"]].copy()
df_copy.head()
print(df_copy.head())
'''
you could have used also the function _get_numeric_data() instead 
of explicitly selecting 
 
 Data Preperation
----------------------------
Let's start by creating: 
1. matrix X that will contain   only the features,
2. vector y with all the labels.  The Recommended IND column
   the customer recommends buying  
   '1' = recommend   '0' = not recommend.

'''
# X= TRAINING_FEATURES  = Everthing without the 'Recommended IND' column
TRAINING_FEATURES =  df_copy.columns[df_copy.columns != 'Recommended IND']
TARGET_FEATURE    = 'Recommended IND'

X = df_copy[TRAINING_FEATURES]
y = df_copy[TARGET_FEATURE]
print("\n\n   X \n------------\n",X)
print("\n\n   y \n------------\n",y)

#The split ratio is given by the test_size parameter
# in the train_test_split function.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Initial amount of samples: #{}".format(X.shape[0]))
print("Number of training samples: #{}".format(X_train.shape[0]))
print("Number of test samples: #{}".format(X_test.shape[0]))

print("\nTarget distribution in original dataset:\n{}".format(y.value_counts()))
print("\nTarget distribution in the training set:\n{}\n".format(y_train.value_counts()))
print("Target distribution in the test set:\n{}".format(y_test.value_counts()))

scaler = StandardScaler()
# z=(x - u) / s #  z=standard score  u = mean   s = standard deviation
 
#********************

X_train_scaled = scaler.fit_transform(X_train)
print("X_train_scaled    Mean: ", X_train_scaled.mean(axis=0))
print("X_train_scaledStandard  Deviation: ", X_train_scaled.std(axis=0))

#Apply it on the test set
X_test_scaled = scaler.transform(X_test)

#Check X_train_scaled's mean and standard deviation
print("X_test_scaled    Mean: ", X_test_scaled.mean(axis=0))
print("X_test_scaled    Standard Deviation: ", X_test_scaled.std(axis=0))

'''
We only applied the transform method, since we learned already the 
normalization values from the train set before.
The standard deviation is not exactly 1 as in the training set and the 
mean is not as close to 0 as in the training set as well - but it is close.
'''

'''
check the MinMaxScaling option.
---------------------
Let's assume we want all our values in a range of 0 and 1 -
 we just have to input these values into our transformer.
'''
min_max_scaler = MinMaxScaler(feature_range=(0, 1))
X_train_scaled_in_range = min_max_scaler.fit_transform(X_train)
print("Min Value: ", X_train_scaled_in_range.min(axis=0))
print("Max Value: ", X_train_scaled_in_range.max(axis=0))
X_test_scaled_in_range = min_max_scaler.transform(X_test)


'''
Normalizing 
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/6c93ec048fa047efbef02828a32bb0d0/b37f098fbe18488e865593740c38e5ea/?child=last


Apply Machine Learning Algorithm - Train
------------------------------------------- 
We will use the LogisticRegression algorithm.

Apply the train  function fit.
 We pass:
    1. feature matrix (X -  X_trainX_train )
    2. label series   (y -  y_trainy_train ).
 The output of the fit function is a model.

'''

#    LogisticRegression algorithm,
clf_model = LogisticRegression().fit(X_train, y_train)
# Use the classifier model (clf_model)  and apply it  on new data (X_test) in
# order to predict its labels
y_pred=clf_model.predict(X_test)
'''
In order to evaluate the model, we will compare the predicted labels, to the
 actual labels provided by y_test, using a DataFrame 
'''

resDF=pd.DataFrame({"Actual":y_test,"Predicted":y_pred})

#  ^: exclusive-or (bitwise)
resDF["correct"]= abs((resDF["Actual"]^resDF["Predicted"])-1)
# for every correct prediction put 1 in the columnn
resDF[resDF["correct"]==1]
print("  resDF \n--------------\n", resDF)

print("correct:",len(resDF[resDF["correct"]==1]))
print("total:",len(resDF))
print("correct %:",len(resDF[resDF["correct"]==1])/len(resDF))


# if you want to have in the train set 70%  of the instances?
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\n\nChange train set 70%  of the instances\n---------------------")
print("Initial amount of samples: #{}".format(X.shape[0]))
print("Number of training samples: #{}".format(X_train.shape[0]))
print("Number of test samples: #{}".format(X_test.shape[0]))
print("\nTarget distribution in original dataset:\n{}".format(y.value_counts()))
print("\nTarget distribution in the training set:\n{}\n".format(y_train.value_counts()))
print("Target distribution in the test set:\n{}".format(y_test.value_counts()))

# if you want all feature values to be between -5 and 5?
print("\n\nall feature values to be between -5 and 5\n------------------------")
min_max_scaler = MinMaxScaler(feature_range=(-5, 5))
X_train_scaled_in_range = min_max_scaler.fit_transform(X_train)
print("Min Value: ", X_train_scaled_in_range.min(axis=0))
print("Max Value: ", X_train_scaled_in_range.max(axis=0))

X_test_scaled_in_range = min_max_scaler.transform(X_test)

#Send the updated features to the machine learning algorithm
# evaluate the results.
# Are they better? worse? what do you think are the reasons for the change?

clf_model = LogisticRegression().fit(X_train, y_train)

y_pred=clf_model.predict(X_test)

resDF=pd.DataFrame({"Actual":y_test,"Predicted":y_pred})

resDF["correct"]=abs((resDF["Actual"]^resDF["Predicted"])-1)
print("correct:",len(resDF[resDF["correct"]==1]))
print("total:",len(resDF))
print("correct %:",len(resDF[resDF["correct"]==1])/len(resDF))

#An introduction to Machine Learning
#https://www.geeksforgeeks.org/introduction-machine-learning/