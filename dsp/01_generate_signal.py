#!/usr/bin/env python3
'''
 עיבוד אותות דיגיטלי עם פייתון 01 יצירת סיגנל
https://www.youtube.com/watch?v=aAaPoOjJPow&list=PLeXm9_pfh4dz0fT_pPCS2WpeorfqAGg6B&index=1
 https://github.com/Metallicode/python_dsp
 https://github.com/Metallicode/python_dsp/blob/master/01_generate_signal.py
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


sample_rate = 44100
frequency = 200# Hrz
# Time data

total_signal_length = 2.0# length in seconds
start = 0
end = total_signal_length

step = total_signal_length/sample_rate

#x aix
t = np.arange(start, end ,step)
print("len(t) = ",len(t))


#y_aix
signal1 = np.sin(2 * np.pi * frequency * t)


#Build a squre wave   10:08
signal2 = (np.mod(frequency*t,1) < 0.5)*2.0-1
print(signal2)
noise = 1.0*np.random.randn(*signal2.shape)

####PLOT SIGNAL####

plt.plot(t, signal1,'black')
plt.plot(t, signal2,'red')
signal3 = signal2+noise
plt.plot(t, signal3,'orange');
plt.show()



####WRITE AUDIO FILE####
signal3 *= 32767
signal3 = np.int16(signal3)

 

wavfile.write("test.wav", sample_rate, signal3)
