#!/usr/bin/env python3
'''
     02 עירבול אותות (מיקס) ונירמול ערכים
 https://www.youtube.com/watch?v=xS1KAxpzapE&list=PLeXm9_pfh4dz0fT_pPCS2WpeorfqAGg6B&index=2
 https://github.com/Metallicode/python_dsp
 https://github.com/Metallicode/python_dsp/blob/master/02_add_noise.py
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#normalize function
def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1

###SET sample rate & signal frequency
sample_rate = 44100 # samples per  seconed
frequency = 5 #Hz
start = 0
end = 1.0
step = (end - start)/sample_rate
t = np.arange(start, end , step)

####PRODUCE SIGNALS
sin_signal = np.sin(2 * np.pi * frequency * t)
signal = (np.mod(frequency*t,1) < 0.5)*2.0-1
print("*signal.shape = ",*signal.shape)
noise = 1.0*np.random.randn(*signal.shape)
dirty = signal + noise
dirty_sin = sin_signal + noise
####COMBINE NOISE AND SIGNAL (and normalize array...)
dirty_norm =  norm(dirty)
dirty_sin_norm = norm(dirty_sin)
x = np.arange(1000)
y = np.abs(np.fft.ifft(dirty_norm))[:1000]
y_sin = np.abs(np.fft.ifft(dirty_sin_norm))[:1000]

####PLOT SIGNAL####
plt.subplot(411)
plt.plot(t, dirty,'orange');
plt.title('signal + noise')
plt.subplot(412)
plt.plot(t, dirty_norm,'black');
plt.title('normalize(signal + noise)')

plt.subplot(413)
plt.plot(x, y,'red')
#plt.plot(np.arange(1000),np.abs(np.fft.ifft(dirty_norm))[:1000],'red')

plt.title('np.fft.ifft(signal + noise)')


plt.subplot(414)
plt.plot(x, y_sin,'blue')
#plt.plot(np.arange(1000),np.abs(np.fft.ifft(dirty_norm))[:1000],'red')

plt.title('np.fft.ifft(sin + noise)')
plt.show()

####WRITE AUDIO FILE####
dirty_norm *= 32767
dirty_norm = np.int16(dirty_norm)
wavfile.write("file.wav", sample_rate, dirty_norm)

