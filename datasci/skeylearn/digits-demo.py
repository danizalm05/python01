
'''
#
https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py
https://scikit-learn.org/stable/tutorial/basic/tutorial.html
An introduction to machine learning with scikit-learn
------------------------------------------------------------
Recognize images of hand-written digits, from 0-9.
The task is to predict, given an image, which digit it represents.
digits.images = arrays of 8X8 images of
digits.target = the numbers 0-9

'''
from sklearn import datasets
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()
# For image files (e.g., ‘png’ files), use matplotlib.pyplot.imread.

#  digits.data gives access to the features that can be
#  used to classify the digits samples
print("\ndigits.data\n---------\n",digits.data)
print("\ndigits.target\n-------\n",digits.target)
#print("\ndigits.images[0]\n-------------\n",digits.images[0])

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
plt.show()

'''
 We are given samples of each of the 10 possible classes 
 (the digits zero through nine) on which we fit an estimator
 to be able to predict the classes to which unseen samples belong.
 
 An "estimator" is a statistic (that is, a function of the data) that 
 is used  to infer the value of an unknown parameter in a 
 statistical model.
 
 In scikit-learn, an estimator for classification is a Python object 
 that implements the methods fit(X, y) and predict(T).

 

'''
#An example of an estimator is the class sklearn.svm.SVC

'''
The  estimator (clf), must learn from the model.
  
'''

# flatten the images
'''
Flatten the images, turning each 2-D array of grayscale values from 
shape (8, 8) into shape (64,).
 Subsequently, the entire dataset will be of shape
  (n_samples, n_features), 
where n_samples is the number of images and n_features is the total 
number of pixels in each image.


'''
print("\ndigits.images[0]\n--------\n",digits.images[0])
#digits.images is an array of the length of 'n_samples' items for each
# image each item is 8X8 array
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
#(-1)means that  you are asking numpy to suggest  number of column
# or rows to get reshaped in.
#data is an array of the length of 'n_samples' items for each image
#each item is 64 numbers
print("\n data\n--------\n",data[1])
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
