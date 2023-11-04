'''
             Nearest Neighbors Classification -  version 2
How to use KNeighborsClassifier. We train such a classifier on the iris dataset
 and observe the difference of the decision boundary obtained with regards to
 the parameter weights.

https://scikit-learn.org/stable/tutorial/statistical_inference/
https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html

https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html
https://scikit-learn.org/stable/glossary.html#glossary

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
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


iris = load_iris(as_frame=True)
print("\n\niris.DESCR\n-----------\n",iris.DESCR)
X = iris.data[["sepal length (cm)", "sepal width (cm)"]]
y = iris.target
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

'''            k-Nearest neighbors classifier   version  2
---------------------------------------------------------
 
'''
# We want to use a k-nearest neighbors classifier considering
# a neighborhood of 11 data points.
#Pipeline Sequentially apply a list of transforms and a final estimator.
#Use a Pipeline to chain a scaler before to use our classifier.
#  StandardScaler() = scale the data beforehand
clf = Pipeline(
    steps=[("scaler", StandardScaler()),
           ("knn", KNeighborsClassifier(n_neighbors=11))]
)


'''
Fit two classifiers with different values of the parameter weights. We 
plot the decision boundary  of each classifier as well as the original
 dataset to observe the difference.
'''
from sklearn.inspection import DecisionBoundaryDisplay

_, axs = plt.subplots(ncols=2, figsize=(12, 5))
# weights =  ("uniform", "distance")
for ax, weights in zip(axs, ("uniform", "distance")):
    clf.set_params(knn__weights=weights).fit(X_train, y_train)
    disp = DecisionBoundaryDisplay.from_estimator(
        clf,
        X_test,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
        alpha=0.5,
        ax=ax,
    )
    scatter = disp.ax_.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, edgecolors="k")
    disp.ax_.legend(
        scatter.legend_elements()[0],
        iris.target_names,
        loc="lower left",
        title="Classes",
    )
    _ = disp.ax_.set_title(
        f"3-Class classification\n(k={clf[-1].n_neighbors}, weights={weights!r})"
    )

plt.show()