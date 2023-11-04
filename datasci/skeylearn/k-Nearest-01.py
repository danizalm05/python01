'''
                          Supervised learning
Predicting an output variable from high-dimensional observations
https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
https://scikit-learn.org/stable/glossary.html#glossary

Supervised learning consists in learning the link between two datasets:
 X: the observed data
 y: a variable  we are trying to predict, called “target” or “labels”.
  Most often, y is a 1D array of length n_samples.

An estimator = object that learns from data;
All supervised estimators in scikit-learn implement the next two methods:
 1.  fit(X, y) method to fit the model
 2.  predict(X) method that, given unlabeled observations X,  returns the
      predicted labels y.

'''

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
'''
        Prediction task   
---------------------------
1. classification task =  classify the observations in a set of finite labels,
    in other words to “name” the objects observed. 
2. regression task = predict a continuous target variable 
 
'''
# The iris dataset is a classification task consisting in identifying 3
# different types of irises (Setosa, Versicolour,
# and Virginica) from their petal and sepal length and width:
iris = datasets.load_iris()
iris_X, iris_y = datasets.load_iris(return_X_y=True)
y= np.unique(iris_y) #only diffrent values 0,1,2
print( y) # output is:  the array  [0, 1, 2]

'''            k-Nearest neighbors classifier
---------------------------------------------------------
Given a new observation X_test, find in the training set 
the observation with the closest feature vector.  
'''
# Split iris data in train and test data

np.random.seed(0)  # A random permutation, to split the data randomly
indices = np.random.permutation(len(iris_X))

iris_X_train = iris_X[indices[:-10]]#All but last 10 item
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]#Just last 10 item
iris_y_test = iris_y[indices[-10:]]
print(iris_y_test  )
 # Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier(n_neighbors=11)
#knn = KNeighborsClassifier()
fitForKNN = knn.fit(iris_X_train, iris_y_train)
print("fitForKNN =",fitForKNN)

prde = knn.predict(iris_X_test)
print ("Predict values = ",prde)
print("Real values = ",iris_y_test)


import matplotlib.pyplot as plt

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()