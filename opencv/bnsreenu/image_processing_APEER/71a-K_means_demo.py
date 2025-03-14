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

plt.show()
