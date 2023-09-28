""" 2:00
Extracting Mel-Frequency Cepstral Coefficients with Python
MFCCs are a fundamental audio feature.
How to extract MFCCs (and 1st and 2nd MFCCs derivatives) from an audio file
 with Python and Librosa.



https://github.com/musikalkemist/AudioSignalProcessingForML/blob/master/20-%20Extracting%20MFCCs%20with%20Python/Extracting%20MFCCs.ipynb
https://www.youtube.com/watch?v=WJI-17MNpdE&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=21
https://librosa.org/doc/latest/index.html

"""
import os
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

BASE_FOLDER = "C:/Users/rockman/Music/wav"
debussy_file = os.path.join(BASE_FOLDER, "debussy.wav")
redhot_file = os.path.join(BASE_FOLDER, "redhot.wav")
duke_file = os.path.join(BASE_FOLDER, "duke.wav")




#ipd.Audio(debussy_file)

# load audio files with librosa
signal, sr = librosa.load(debussy_file)

#Extracting MFCCs
mfccs = librosa.feature.mfcc(y=signal, n_mfcc=13, sr=sr)

print(" mfccs.shape = ", mfccs.shape)

# Visualising MFCCs

plt.figure(figsize=(25, 10))
librosa.display.specshow(mfccs,
                         x_axis="time",
                         sr=sr)
plt.colorbar(format="%+2.f")
plt.show()

#Computing first / second MFCCs derivatives
delta_mfccs = librosa.feature.delta(mfccs)

delta2_mfccs = librosa.feature.delta(mfccs, order=2)

print('delta_mfccs.shape = ',delta_mfccs.shape)



plt.figure(figsize=(25, 10))
librosa.display.specshow(delta_mfccs,
                         x_axis="time",
                         sr=sr)
plt.colorbar(format="%+2.f")
plt.show()

plt.figure(figsize=(25, 10))
librosa.display.specshow(delta2_mfccs,
                         x_axis="time",
                         sr=sr)
plt.colorbar(format="%+2.f")
plt.show()

mfccs_features = np.concatenate((mfccs, delta_mfccs, delta2_mfccs))

print("mfccs_features.shape = ", mfccs_features.shape)


