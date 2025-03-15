"""
71-K_means.py
71a-K_means_demo.py

The KMeans algorithm clusters data by trying to separate samples
in n groups of equal variance, minimizing a criterion known as 
the inertia or within-cluster sum-of-squares 
 -------------------------------------------
https://www.youtube.com/watch?v=H_L7V_BH9pc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=73


https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial71a-K_means_demo.py
 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_blobs

# create simulated clusters using scikit learn's make_blobs
data, true_cluster = make_blobs(n_samples=500, 
                                centers=3,
                                random_state=0, 
                                cluster_std=0.60) 

data_df = pd.DataFrame(data)
data_df.columns=['x','y']
data_df['true_cluster'] = true_cluster
data_df.head(n=3)

color_map= {0:'purple',1:'blue',2:'yellow'}
data_df['true_color'] = data_df.true_cluster.map(color_map)
data_df.head(n=3)


plt.scatter(x='x',y='y',c='true_color',data=data_df)
plt.xlabel("x")#add  'y' label  on y-aix
plt.ylabel("y")
plt.title("Simulated clusters using scikit learn")
plt.show()

#  Chose randomly a center of the group
#------------------------------------------------
#data_df.sample: Return a random sample of items from an axis of object.
#You can use random_state for reproducibility.

current_centers = data_df.sample(3,random_state=42)
plt.scatter(x='x',y='y',
           c='yellow',
           data=data_df)
plt.scatter(x='x',y='y', 
           data=current_centers,
           c=['red','blue','green'],
           s=100)
plt.xlabel("x")
plt.ylabel("y")

plt.title("current_centers")
plt.show()

##########################################
# distance
def dist(x, y):
    return sum((xi - yi) ** 2 for xi, yi in zip(x, y))

def assign_cluster_labels(data, centers):
    cluster_labels = []
    for point in data:
        # compute distances between three cluster centers to a data point
        distances = [dist(point, center) for center in centers]
        # find which cluster is closest to the data point and assign the cluster  it
        cluster_labels.append(distances.index(min(distances)))
    return cluster_labels


current_labels = assign_cluster_labels(data_df[['x','y']].values, 
                                      current_centers[['x','y']].values)
current_labels[1:3]
#[2, 0, 0, 0, 0, 2, 0, 0, 0, 0]

plt.scatter(x='x',y='y',c=current_labels,data=data_df)
plt.scatter(x='x',y='y',data=current_centers,c=['red','blue','black'],marker='*', s=200)
plt.title("Distance")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#Second iteration
current_centers = data_df[['x','y']].groupby(current_labels).mean()
print(current_centers)
current_labels = assign_cluster_labels(data_df[['x','y']].values, 
                                      current_centers.values)
 
plt.scatter(x='x',y='y',c=current_labels,data=data_df)
plt.scatter(x='x',y='y',data=current_centers,c=['red','blue','black'],marker='*', s=200)
plt.title("Second iteration  -  groupby mean")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#3rd iteration
current_centers = data_df[['x','y']].groupby(current_labels).mean()
print(current_centers)
current_labels = assign_cluster_labels(data_df[['x','y']].values, 
                                      current_centers.values)
 
plt.scatter(x='x',y='y',c=current_labels,data=data_df)
plt.scatter(x='x',y='y',data=current_centers,c=['red','blue','black'],marker='*', s=200)
plt.xlabel("x")
plt.xlabel("y")
plt.show()
#4th iteration

current_centers = data_df[['x','y']].groupby(current_labels).mean()
print(current_centers)
current_labels = assign_cluster_labels(data_df[['x','y']].values, 
                                      current_centers.values)
 
plt.scatter(x='x',y='y',c=current_labels,data=data_df)
plt.scatter(x='x',y='y',data=current_centers,c=['purple','blue','yellow'],marker='*', s=200)
plt.xlabel("x")
plt.xlabel("y")
plt.show()