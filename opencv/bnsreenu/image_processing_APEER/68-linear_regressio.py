"""
tutorial68-linear_regression.py
 -------------------------------------------
https://www.youtube.com/watch?v=9CxJhQynU20&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=70
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial68-linear_regression.py

db source:
https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/cells.csv

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/cells.csv')
print(df)
plt.scatter(x="time", y="cells", data=df)
plt.show()