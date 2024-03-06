#!/usr/bin/env python3
'''
Decision Trees
     Build a decision tree classifier (using DecisionTreeClassifier)
    Learn how to visualize Decision Trees
    Handling overfitting - analyze tradeoffs between different pruning parameters
    Introduce Random forests (using RandomForestClassifier)
n this notebook we'll use a dataset of Titanic passengers and develop a model to predict whether
a particular passenger will survive or not.


you may need to run the following command: pip install pydotplus
In order to use the classifier we already did some preprocessing such as:

    Converting categorical values to numerical values (Sex: Male-1, Female-0,
    Embarked: S-0, C-1,Q-2)
    Age has missing values. Let's assume that a person with missing age is of mean age
     (this is one possible..).
    Embarked has missing values, we add a dedicated category for unknown embarkation points.
    Omited irrelvant values for classification (passengerID, Name, Ticket and Cabin).


 https://courses.campus.gov.il/courses/course-v1:HIT+ACD_RFP4_DataScienceIntro_HE+2022_1/courseware/f47ba54cd6974a76a3f8b3c30ed60ac2/8095a30562f0481dbfa747eb905427eb/3?activate_block_id=block-v1%3AHIT%2BACD_RFP4_DataScienceIntro_HE%2B2022_1%2Btype%40html%2Bblock%408afb735e82854a48ad68d72d85a9a013
 https://labs.vocareum.com/main/main.php?m=editor&asnid=537374&stepid=537375&hideNavBar=1

'''
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

titanic = pd.read_csv('./data/titanic_preprocessed.csv' )  # load data
print("titanic_preprocessed.csv\n------------\n\n",titanic.head(10))
# initial description of the data
print("\n\ntitanic.describe()\n--------------\n",titanic.describe())
'''Sklearn has a nice decision tree implementation which we'll use to learn 
   a tree for our Titanic dataset.
Before we start building our trees , we will define 2 helper functions:




'''
#splitData   returns a train test split,   only the listed attributes appear in the X  matrix
def splitData(features):
    """Split a subset of the titanic dataset, given by the features, into train and test sets."""
    titanic_predictors = titanic[features].values
    titanic_labels = titanic["Survived"].values

    # Split into training and test sets
    XTrain, XTest, yTrain, yTest = train_test_split(titanic_predictors, titanic_labels, random_state=1, test_size=0.5)
    return XTrain, XTest, yTrain, yTest

#RenderTree - render (draw) the visualization of a tree
from IPython.display import Image, display
import pydotplus
from scipy import misc


def renderTree(my_tree, features):
    # hacky solution of writing to files and reading again
    # necessary due to library bugs
    filename = "temp.dot"
    with open(filename, 'w') as f:
        f = tree.export_graphviz(my_tree,
                                 out_file=f,
                                 feature_names=features,
                                 class_names=["Perished", "Survived"],
                                 filled=True,
                                 rounded=True,
                                 special_characters=True)

    dot_data = ""
    with open(filename, 'r') as f:
        dot_data = f.read()

    graph = pydotplus.graph_from_dot_data(dot_data)
    image_name = "temp.png"
    graph.write_png(image_name)
    display(Image(filename=image_name))

 # After we are done with the prep, let's start building out first, yet very simple tree
 # - one that ONLY operates on sex!

decisionTree = tree.DecisionTreeClassifier()

XTrain, XTest, yTrain, yTest = splitData(["Sex"])
# fit the tree with the traing data
decisionTree = decisionTree.fit(XTrain, yTrain)

# predict with the training data
y_pred_train = decisionTree.predict(XTrain)
# measure accuracy
print('Accuracy on training data = ',
      metrics.accuracy_score(y_true=yTrain, y_pred=y_pred_train))

# predict with the test data
y_pred = decisionTree.predict(XTest)
# measure accuracy
print('Accuracy on test data = ',
      metrics.accuracy_score(y_true=yTest, y_pred=y_pred))

renderTree(decisionTree, ["Sex"])
#Accuracy on test data = ~76%     (correct on the test set, isn't bad! )
# sex seems to be a very good indicator of whether someone has survived or not.



#  train tree on sex and the number of the number of siblings/spouses aboard
used_features = ["Sex", "SibSp"]
XTrain, XTest, yTrain, yTest = splitData(used_features)
decisionTree = tree.DecisionTreeClassifier()
decisionTree = decisionTree.fit(XTrain, yTrain)

y_pred_train = decisionTree.predict(XTrain)
print('Accuracy on training data= ', metrics.accuracy_score(y_true = yTrain, y_pred = y_pred_train))

y_pred = decisionTree.predict(XTest)
print('Accuracy on test data= ', metrics.accuracy_score(y_true = yTest, y_pred = y_pred))
#