'''
Statistical-learning for scientific data processing
Scikit-learn is a Python module integrating classic machine learning algorithms
 in the tightly-knit world of scientific Python packages
 (NumPy, SciPy, matplotlib).

https://scikit-learn.org/stable/tutorial/statistical_inference/index.html

https://scikit-learn.org/stable/glossary.html#glossary


Scikit-learn deals with learning information from one or more datasets that are
represented as 2D arrays. They can be understood as a list of multi-dimensional
observations.
 We say that the first axis of these arrays is the samples axis, while the
 second is the features axis.
'''

from sklearn import datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
data = iris.data
print("\n\ndata.shape\n-----------\n",data.shape)
#It is made of 150 observations of irises, each described by 4 features:
#their sepal and petal length and width, as detailed in iris.DESCR
print("\n\n data[0]",data[0])

print("\n\niris.DESCR\n-----------\n",iris.DESCR)

'''
                        Reshaping data 
When the data is not initially in the (n_samples, n_features) shape, it needs 
to be preprocessed in order to be used by scikit-learn.
An example of reshaping data would be the digits dataset
he digits dataset is made of 1797 8x8 images of hand-written digits
'''

digits = datasets.load_digits()
print("before  reshaped",digits.images.shape)
# The shape is (1797, 8, 8) it should be (1797,64)
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)
plt.show()
'''
To use this dataset with scikit-learn, we transform 
each 8x8 image into a feature vector of length 64
'''
data = digits.images.reshape( (digits.images.shape[0], -1))
print("after reshaped ",data.shape)

'''
                    Estimators objects
An estimator = object that learns from data; it may be a classification, 
 regression or clustering algorithm or a transformer that 
 extracts/filters useful features from raw data.
All estimator objects expose a fit method that takes a dataset (usually 2d array) 

estimator.fit(data)

All the estimated parameters are attributes of the estimator object ending 
by an underscore:
>>> estimator.estimated_param_ 
'''

