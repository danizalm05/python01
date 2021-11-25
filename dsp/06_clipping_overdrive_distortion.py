#!/usr/bin/env python3
'''
clipping & overdrive

github.com/Metallicode/python_dsp
https://www.youtube.com/watch?v=LX06jw7VI3w&list=PLeXm9_pfh4dz0fT_pPCS2WpeorfqAGg6B&index=6

https://github.com/Metallicode/python_dsp/blob/master/06_clipping_overdrive_distortion.py
https://matplotlib.org/stable/gallery/index.html
 '''

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile



#normalize function
def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1

