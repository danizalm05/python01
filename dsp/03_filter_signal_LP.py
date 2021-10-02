#!/usr/bin/env python3
'''
עיבוד אותות דיגיטלי עם פייתון 03 סינון תדרים גבוהים LP Filter
 https://www.youtube.com/watch?v=hGgLpwBi_Ps&list=PLeXm9_pfh4dz0fT_pPCS2WpeorfqAGg6B&index=3
 https://github.com/Metallicode/python_dsp
 https://github.com/Metallicode/python_dsp/blob/master/03_filter_signal_LP.py
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

cutoff = 50
alpha = cutoff / (sample_rate/2)


dirty0 = LPF(dirty,alpha)

sr, data = wavfile.read("sample.wav")# sr = sample rate
dirty1 = norm(data)
dirty2 = LPF(dirty1,alpha)

####PLOT SIGNAL####
plt.subplot(3, 2, 1)# 3 row, 2 columns, and this plot is the 1's.
plt.plot(t, dirty0,'orange')
plt.suptitle("MY SHOP")
plt.title('dirty0:square + noise')
plt.subplot(3, 2, 2)# 3 row, 2 columns, and this plot is the 2'nd.
plt.plot(t, dirty1[:len(t)],'red')
plt.title('dirty1: sample.wav')
plt.subplot(313)
plt.plot(t, dirty2[:len(t)],'red')
plt.title('dirty2: LPF(sample.wav,alpha)')
plt.show()


####PLOT SIGNAL IN FREQUENCY DOMAIN####
plt.plot(np.arange(20000),np.abs(np.fft.ifft(norm(data)))[:20000],'blue')
plt.plot(np.arange(20000),np.abs(np.fft.ifft(dirty2))[:20000],'red')
plt.title('Compre: sample.wav to LPF(sample.wav,alpha)')
plt.show()