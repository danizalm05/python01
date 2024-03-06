#!/usr/bin/env python3
'''
MNIST handwritten digits
https://labs.vocareum.com/main/main.php?m=editor&asnid=537378&stepid=537379&hideNavBar=1
https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/f47ba54cd6974a76a3f8b3c30ed60ac2/65cf25ad983746af8b0941197cd00926/2?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40lti_consumer%2Bblock%4023aa3f2998894298b9efa1ac6f6d24ab
THE MNIST handwritten digit dataset consists of images of handwritten digits, together
with labels indicating which digit is in each image.


we'll use scikit-learn to compare classification methods on the MNIST dataset.

There are several versions of the MNIST dataset. We'll use the one that is built-into
 scikit-learn, described here.
    Features: integers 0-16 (grayscale value; 0 is white, 16 is black)


Note that we will scale the data before running them through our algorithms.
You can read details about scaling and why it's important in the below URL:
scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling.

'''
import pandas as pd
import numpy as np

from sklearn import tree, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale


import matplotlib.pyplot as plt
#%matplotlib inline
plt.rcParams['figure.figsize'] = (10, 6)
plt.style.use('ggplot')
digits = load_digits()
X = digits.data
y = digits.target
print(type(X))

n_samples, n_features = X.shape
n_digits = len(np.unique(digits.target))
print("n_digits: %d, n_samples %d, n_features %d" % (n_digits, n_samples, n_features))
# this is what one digit (a zero) looks like

print("===\nThe digit")
print(digits.target[0])

print("===\nThe raw data")
print(digits.images[0])

print("===\nThe scaled data")
print(X[0])

plt.figure(figsize= (10, 10))
for ii in np.arange(25):   # first 25 numbers
    plt.subplot(5, 5, ii+1)
    plt.imshow(np.reshape(digits.images[ii,:],(8,8)), cmap='Greys',interpolation='nearest')
    plt.axis('off')
plt.show()
'''
Task: Classification with different algorithms
------------------------------------------------------
   1. Split the data into a training and test set using the command
   2. train_test_split(X, y, random_state=1, test_size=0.8)
   3. Use various algorithms such as: DT, RandomForest, NB and knn to build a classifier 
     using the training dataset.
    Using the test dataset, evaluate the accuracy of the model. Again using the test dataset,
     compute the confusion matrix. What is the most common mistake that the classifier makes?
      What are the differences between the algorithms
    Using the 'cross_val_score' function, evaluate the accuracy of the DT with various
     depth and split items, and various K values in kNN? (Hint you may want to use 
     GridSearchCV for that)
    Try to train and test the algorithm on the raw (non-scaled) data. What's your accuracy score?

optional
    print and visualize all misclassified images
    2:01
'''
XTrain, XTest , yTrain , yTest = train_test_split(X, y, random_state = 1, test_size = 0.8)

clf1 = tree.DecisionTreeClassifier()
clf2 = RandomForestClassifier()
clf3 = GaussianNB()
clf4 = KNeighborsClassifier(n_neighbors =5)
#5:40
algNames = ["decision tree", "random forest", "naive bayes","knn"]
print("\n")
for idx,clf in enumerate( [clf1,clf2,clf3,clf4] ):
     clf.fit(XTrain, yTrain) #6:49
     yPred = clf.predict(XTest)
     yPredTrain = clf.predict(XTrain)#8:42
     print (idx,": ",algNames[idx])
     print(clf,"Classifier","\n------------------------------")
     print("train accuracy = ", metrics.accuracy_score(y_true=yTrain,y_pred=yPredTrain))
     print("Test accuracy = ", metrics.accuracy_score(y_true=yTest,y_pred=yPred))
     print("Confusion matrix \n", metrics.confusion_matrix(yTest,yPred))
     print("\n")

     #  chapter 2
     #Using the 'cross_val_score' function, evaluate the accuracy of the DT with various depth
     # and  split items, and various K values in kNN?
     # (Hint you may want to use GridSearchCV   for that)

     from sklearn.model_selection import GridSearchCV
     #scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
     clf = tree.DecisionTreeClassifier()
     params = {"max_depth": [2,4,6],"min_samples_split":[10,15,20]}
     clfCV = GridSearchCV(clf,params,cv=10 )
     clfCV.fit(X,y) #1:48