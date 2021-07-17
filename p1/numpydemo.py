"""Numpy arrays are great alternatives to Python Lists. Some of the key advantages
of Numpy arrays are that they are fast, easy to work with, and give users the
opportunity to perform calculations across entire arrays.

In the following example, you will first create two Python lists.
Then, you will import the numpy package and create numpy arrays out of the
newly created lists.
"""
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print('bmi = ',bmi)




# Print only those observations above 23
print('bmi > 27 = ',bmi[bmi > 27])

# Convert the list of weights from a list to a Numpy array
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)  # Create a numpy array np_weight_kg from weight_kg
# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print('np_weight_lbs = ', np_weight_lbs)
