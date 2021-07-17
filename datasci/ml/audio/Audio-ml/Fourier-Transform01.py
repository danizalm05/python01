""" 15:00
 Demystifying the Fourier Transform: The Intuition
https://www.youtube.com/watch?v=XQ45IgG6rJ4&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=11
https://github.com/musikalkemist/AudioSignalProcessingForML/tree/master/10%20-%20Fourier%20Transform:%20The%20Intuition

https://librosa.org/doc/latest/index.html

   

https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/yamnet.ipynb?skip_cache=true#scrollTo=Wo9KJb-5zuz1
https://drive.google.com/drive/my-drive
 """
"""
Intuition 
● Compare signal with sinusoids of various frequencies
● For each frequency we get a magnitude 
and a phase 
● High magnitude indicates high similarity between the signal 
and a sinusoid

"""
 
import os
import librosa
import librosa.display
import scipy as sp

import matplotlib.pyplot as plt
import numpy as np




BASE_FOLDER = "C:/Users/rockman/Music/wav"
piano_c_file = os.path.join(BASE_FOLDER, "piano_c.wav")



# load audio file
signal, sr = librosa.load(piano_c_file)

plt.figure(figsize=(18, 8))
librosa.display.waveplot(signal, sr=sr, alpha=0.5)
plt.show()

# derive spectrum using FT
ft = sp.fft(signal)
magnitude = np.absolute(ft)
frequency = np.linspace(0, sr, len(magnitude))

plt.figure(figsize=(18, 8))
plt.plot(frequency[:5000], magnitude[:5000]) # magnitude spectrum
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("C5 FFT spectrum (C5 freq = 500)")
plt.show()

print("Number of  samples = ", len(signal))
d = 1 / sr # Duration of  each sample
print("Duration of each sample = ", d)

d_523 = 1 / 523 # Duration of cycle of funmental  frequncy
print("Duration of funmental  frequncy = ", d_523)

d_400_samples = 400 * d  #Duration of 400  samples

print("Duration of 400  samples = ", d_400_samples)

# zomm in to the waveform
samples = range(len(signal))
t = librosa.samples_to_time(samples, sr=sr)

plt.figure(figsize=(18, 8))
plt.plot(t[10000:10400], signal[10000:10400])  #400 samples
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()