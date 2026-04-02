# -*- coding: utf-8 -*-
"""
    image-classification-python-scikit-learn
https://youtu.be/il8dMDlXrIE?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=339
https://youtu.be/il8dMDlXrIE?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=1125
https://github.com/computervisioneng/image-classification-python-scikit-learn/blob/master/main.py

data:
  https://drive.google.com/drive/folders/1CjEFWihRqTLNUnYRwHXxGAVwSXF2k8QC
"""

import getpass

import os
import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# prepare data

categories = ['empty', 'not_empty']
input_dir = 'C:/Users/' + getpass.getuser() + '/Pictures/clf-data'
 
#C:\Users\rockman\Pictures\clf-data
data = []
labels = [] 

for category_idx, category in enumerate(categories):
      catg = (os.path.join(input_dir, category))
      for file in os.listdir(catg  ):
          img_path = os.path.join(input_dir, catg, file)
          print(file)
          img = imread(img_path)
          img = resize(img, (15, 15)) 
          data.append(img.flatten())
          labels.append(category_idx)
data = np.asarray(data)
labels = np.asarray(labels)

# train / test split
print("\n------------------ \nsplit  \n")
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
 
# train classifier
classifier = SVC()

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

print("\n------------------ \ntrain  \n")
grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)
  
# test performance
best_estimator = grid_search.best_estimator_

y_prediction = best_estimator.predict(x_test)

score = accuracy_score(y_prediction, y_test)

print('{}% of samples were correctly classified'.format(str(score * 100)))

pickle.dump(best_estimator, open('./model.p', 'wb'))