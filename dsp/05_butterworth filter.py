#!/usr/bin/env python3
'''
05_butterworth filter.py   10:12
עיבוד אותות דיגיטלי עם פייתון 05 Butterworth / Bessel Filters
github.com/Metallicode/python_dsp/blob/master/05_butterworth%20filter.py
github.com/Metallicode/python_dsp
www.youtube.com/watch?v=0ihDl_f5Ebo&list=PLeXm9_pfh4dz0fT_pPCS2WpeorfqAGg6B&index=5

https://matplotlib.org/stable/gallery/index.html

https://scipy.org/
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.bessel.html
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.butter.html
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


def normalize(data):
    mi = min(data)
    ma = max(data)
    return np.array([((x-mi)/(ma-mi)) for x in data])*2.0-1



sample_rate = 44100 # samples per  seconed

start = 0
end = 1.0
step = (end - start)/sample_rate
t = np.arange(start, end , step)
frequency = 5 #Hz
tone1 = np.sin(2 * np.pi* frequency*t)
octaves_number = 20
tone2 = np.sin(2 * np.pi* (frequency* octaves_number ) *t) #   octaves higher
#sum_tone = normalize(tone1 + tone2)
sum_tone =  tone1 + tone2
# butter filter
cutoff = 50
w = cutoff/(44100/2)
order = 4
a, b = signal.butter(order, w, "low", analog=False)
z = signal.filtfilt(a, b, sum_tone)
z = normalize(z)
#  Atter the filter   the higher frequency (tone2) have a lower amplitude

####PLOT SIGNAL####
plt.subplot(3, 2, 1)# 3 row, 2 columns, and this plot is the 1's.

plt.plot(t, tone1,'orange')
plt.suptitle("Signals")
plt.title('tone1')
plt.grid()
plt.subplot(3, 2, 2)# 3 row, 2 columns, and this plot is the 2'nd.
plt.plot(t, tone2,'red')
plt.title('tone2')
plt.grid()
plt.subplot(3, 2, 3)
plt.plot(t, sum_tone ,'red')
plt.title('tone + tone2')

plt.subplot(3, 2, 4)
plt.plot(t, sum_tone ,'red')
plt.plot(t, z ,'black')
plt.grid()
plt.title('signal.butter')


plt.subplot(3, 2, 5)
plt.plot(t, tone1[:len(t)],'blue')
plt.title('signal5: LPF(,alpha=100)')

plt.grid()

plt.subplots_adjust(hspace=0.35)
plt.show()

sr, data = wavfile.read("sample.wav")
data =  tone1
cutoff = 5
w = cutoff/(44100/2)
order = 4

a, b = signal.butter(order, w, "low", analog=False)
z = signal.filtfilt(a, b, data)
z = normalize(z)

a, b = signal.bessel(order, w, "low", analog=False)
q = signal.filtfilt(a, b, data)
q = normalize(q)

fig = plt.figure(figsize=(12,8),dpi=100)

axes = fig.add_axes([0,0,1,1])


axes.plot(np.arange(len(z)), normalize(data), color='pink')
axes.plot(np.arange(len(z)), z, color='black')
axes.plot(np.arange(len(z)), q, color='blue')
# Set max ticks on the x axis
axes.xaxis.set_major_locator(plt.MaxNLocator(8))

# Add a grid, color, dashes(5pts 1 pt dashes separated by 2pt space)
axes.grid(True, color='0.6', dashes=(5, 2, 1, 2))

# Set grid background color
axes.set_facecolor('#FAEBD7')
plt.show()
