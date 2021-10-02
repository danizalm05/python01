#!/usr/bin/env python3
'''
  LP Filter

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def LPF(data,alpha):
    yi = 0
    y = []
    for i in range(len(data)):
        yi += alpha*(data[i]-yi) 
        y.append(yi)
    return y

#normalize function
def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1



###SET sample rate & signal frequency
sample_rate = 44100
frequency = 5 #Hz

t = np.arange(0, 1.0, 1.0/sample_rate)

####PRODUCE SIGNALS
#signal = np.sin(2 * np.pi * frequency * t)
signal = (np.mod(frequency*t,1) < 0.5)*2.0-1
noise = 1.0*np.random.randn(*signal.shape)

####COMBINE NOISE AND SIGNAL (and normalize array...)
dirty =  norm(signal+noise)

cutoff = 5
alpha = cutoff / (sample_rate/2)
dirty5 = LPF(dirty,alpha)

cutoff = 500
alpha = cutoff / (sample_rate/2)
dirty500 = LPF(dirty,alpha)

cutoff = 110
alpha = cutoff / (sample_rate/2)
signal110 = LPF(signal,alpha)



####PLOT SIGNAL####
plt.subplot(3, 2, 1)# 3 row, 2 columns, and this plot is the 1's.

plt.plot(t, signal,'orange')
plt.suptitle("LPF")
plt.title('Original signal')
plt.subplot(3, 2, 2)# 3 row, 2 columns, and this plot is the 2'nd.
plt.plot(t, dirty[:len(t)],'red')
plt.title('dirty0:square + noise')
plt.subplot(3, 2, 3)
plt.plot(t, dirty5[:len(t)],'red')
plt.title('dirty5: LPF(,alpha=5)')
plt.subplot(3, 2, 4)
plt.plot(t, dirty500[:len(t)],'blue')
plt.title('dirty500: LPF(,alpha=500)')


plt.subplot(3, 2, 5)
plt.plot(t, signal110[:len(t)],'blue')
plt.title('signal5: LPF(,alpha=100)')

plt.grid()

plt.subplots_adjust(hspace=0.35)
plt.show()