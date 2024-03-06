'''
#k Nearest Neighbors (k-NN)
#https://labs.vocareum.com/main/main.php?m=editor&asnid=537372&stepid=537373&hideNavBar=1
'''

import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# import data, scikit-learn also has this dataset built-in
iris = load_iris()

# print('The data matrix:\n',iris['data'])
print('The classification target:\n', iris['target'])
print('The names of the dataset columns:\n', iris['feature_names'])
print('The names of target classes:\n', iris['target_names'])
# print('The full description of the dataset:\n',iris['DESCR'])
# print('The path to the location of the data:\n',iris['filename'])
### Dataset visualization

# For easy plotting and interpretation, we only use first 2 features here.
# We're throwing away useful information - don't do this at home!
X = iris.data[:, :2]
y = iris.target  # 3 possible values [0,1,2]

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])  # Colors for mapping values [0,1,2]

# plot data
plt.figure(figsize=(10, 8))

'''
A scatter plot: how two variables relate to each other. 
c= sequence of n numbers to be mapped to colors using cmap and norm.
               #FF0000 -> 0   '#00FF00'  -> 1 , '#0000FF' -> 2
'''
plt.scatter(X[:, 0], X[:, 1], c=y, marker="o", cmap=cmap_bold, s=200)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Iris dataset')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()

# ### Iris dataset classification using KNN

# As you can see, it would be fairly easy to separate the "red" irises from the two classes.
#  However, separating the "green" and "blue" ones would be more challenging.
#
# Let's use KNN to do it.
# But, first let's split the data to train and test
# Split into training and test sets
XTrain, XTest, yTrain, yTest = train_test_split(X, y, random_state=1, test_size=0.2)

# Now we will train the classifier on the train set. As always in sklearn based classifiers,
# we do it using the `fit` function.
# Key question is what $K$ to chose. Let's start with 3

# set up the model, k-NN classification with k = ?
k = 3
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(XTrain, yTrain)

# Let's see how good it is? As you remember, for prediction we will use sklearn's
# `predict` function and apply it on the X matrix of the test set.
# We will then assess its performance by printing the confusion matrix,
# followed by the accuracy score.

y_pred = clf.predict(XTest)

print(metrics.confusion_matrix(y_true=yTest, y_pred=y_pred))

print('Accuracy = ', metrics.accuracy_score(y_true=yTest, y_pred=y_pred))

y_pred = clf.predict(XTest)

print(metrics.confusion_matrix(y_true=yTest, y_pred=y_pred))
print('Accuracy = ', metrics.accuracy_score(y_true=yTest, y_pred=y_pred))

#                             ### Tradeoff's between values of K
#  ** Exercise 1 **
#  Loop to test various values of k (in range of 1 to 20) and see what value or range performs
#  best. Check the accuracy on both: train and test set

k_s=[]
train_accuracies=[]
test_accuracies=[]
for k in range(1,21):
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(XTrain, yTrain)
    y_pred_train=clf.predict(XTrain)
    y_pred=clf.predict(XTest)
    k_s.append(k)
    train_accuracies.append(metrics.accuracy_score(y_true = yTrain, y_pred = y_pred_train))
    test_accuracies.append(metrics.accuracy_score(y_true = yTest, y_pred = y_pred))

df=pd.DataFrame({"k":k_s,"train_accuracy":train_accuracies,"test_accuracy":test_accuracies})
print(df)


# As you see, too low values of $K$ are too specific and yield to over fitting
# (high accuracy on train and low on test),
# as opposed to too high values of $K$ that yield to too simple models
# (low accuracy on both train and test).


# Classification visualization for the knn classifier (based on the selected k).
#  any point in the red area will be classified as the red type, and any point in the green
#  area will be classified as green.
#  You can see that currently it will display the results for `k=1`.
#
# You can then change the code to try different values of $K$ to see how the decision areas
# look like (try at least the values of: 1, 25, 101


k = 101
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X, y)

# plot classification
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),np.linspace(y_min, y_max, 400))
zz = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.pcolormesh(xx, yy, zz, cmap=cmap_light)

# plot data
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,s=30)

plt.title('Classification of Iris dataset using k-NN with k = '+ str(k))
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()


# ### Cross validation

# The simplest way to use cross-validation is to call the `cross_val_score` helper
# function on the estimator and the dataset.
# Cross_val_score is a way of assessing a model and it’s parameters, and cannot be used for
# final training.
# Final training should take place  on all available data and tested using a set of data
# that has been held back from the start.

# The following example demonstrates how to estimate the accuracy of a knn model
# on the iris dataset by splitting the data, fitting a model and computing the
# score 10 consecutive times (with different splits each time).
# Note that the function needs to get as parameters the classifier,
# the feature matrix (X), the labels (y), and a parameter that indicates how many
# folds to execute (cv). The function returns a list with the scores for each fold.

# The splitting of the data set to X group is called "X-fold Cross-validation","

clf = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(clf, X, y, cv=10)
# By default cross_val_score uses a 5-fold strategy,
# however this can be adjusted in the cv parameter.
print("scores = ", scores)
#
# This gave us a list with the accuracy of each iteration.
# If you want to get the overall accuracy, you can simply write:
print("Accuracy: %0.2f" % scores.mean())

# ### Tradeoff's between values of K
## **Excercise 2**
#
# Write a simple loop to test various values of k (in range of 1 to 20)
# and see what value or range performs best. Check the accuracy on both: train and test set


clf = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(clf, X, y, cv=10)
scores_list=[cross_val_score(clf, X, y, cv=flds).mean() for flds in range(3,26)]
print("highest result with X-fold, x=",np.argmax(scores_list)+3)


# ### GridSearchCV ###
#============================
# `GridSearchCV` os class to perofrm cross validation for hyperparameter selection (tuning)
#
# You need to define a dictionary (in the example below called `parameters`), in which
#  you define the possible values for each of the algorithm's parameters. We can use
#  the `scoring` parameter in order to define which evaluation score to optimize.
#  In the example below, we will optimize for accuracy (see the use of the `make_scorer`
#  function with the `accuracy_score`.

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

parameters = {'n_neighbors':range(1,25,2) }
knn = KNeighborsClassifier()
clf = GridSearchCV(knn, parameters,scoring=make_scorer(metrics.accuracy_score, greater_is_better=True))
clf.fit(XTrain, yTrain)

print("best parameter set is:",clf.best_params_," and its score was",clf.best_score_)

#if you want to see all iterations internal numbers uncomment the next line
#print(clf.cv_results_.items())


# I'm sure you appreciate the simplicity of this function instead of doing it manually
# (as in exercise 2...)