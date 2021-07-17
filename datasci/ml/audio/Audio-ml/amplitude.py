
"""
Basic processing operations on audio with Librosa

Load audio files, visualise waveform.
Implement the amplitude envelope feature and see how it differs for
music in different genres.
https://www.youtube.com/watch?v=rlypsap6Wow&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=8

https://librosa.org/doc/latest/index.html

Sound classification with YAMNet
https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/yamnet.ipynb?skip_cache=true#scrollTo=Wo9KJb-5zuz1
https://drive.google.com/drive/my-drive
https://drive.google.com/drive/folders/1BWfonJesCYHvW_Fj7uB_eBQz9PNj2Fm_

librosa
https://drive.google.com/drive/folders/139Yf3r2Ok9MnMUfJOd9Y1xm4maLw86pE
"""



import os
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd


BASE_FOLDER = "C:/Users/rockman/Music/wav"
debussy_file = os.path.join(BASE_FOLDER, "debussy.wav")
redhot_file  = os.path.join(BASE_FOLDER,"redhot.wav")
duke_file    = os.path.join(BASE_FOLDER,"duke.wav")
piano_c5_file= os.path.join(BASE_FOLDER,"piano-c5.wav")


ipd.Audio(debussy_file)


'''load audio files with librosa
  https://librosa.org/doc/latest/generated/librosa.load.html?highlight=load#librosa.load

 librosa.load(path, sr=22050, mono=True, offset=0.0, 
           duration=None, dtype=<class 'numpy.float32'>, res_type='kaiser_best') 
  Returns

   1. ynp.ndarray [ shape=(n,)or(2, n) ]: audio time series
   2. sr number > 0   sampling rate of y
'''

debussy, sr    = librosa.load(debussy_file)
redhot, _      = librosa.load(redhot_file)
duke, _        = librosa.load(duke_file)
piano_c5,sr_5  = librosa.load(piano_c5_file)





print(debussy)
print ("debussy.shape",debussy.shape)
sample_duration = 1 / sr
print(f"One sample lasts for {sample_duration:6f} seconds")
# total number of samples in audio file
tot_samples = len(debussy)

print("Number of samples debussy ",tot_samples)
# duration of debussy audio in seconds
duration = 1 / sr * tot_samples
print(f"The audio lasts for {duration} seconds")

plt.figure(figsize=(15, 17))   

# ------------   Debusy -----------------

plt.subplot(4, 1, 1)
librosa.display.waveplot(debussy, alpha=0.5)
plt.ylim((-1, 1))
plt.title("Debusy")


#-------------   RHCP  ------------
plt.subplot(4, 1, 2)
librosa.display.waveplot(redhot, alpha=0.5)
plt.ylim((-1, 1))
plt.title("RHCP")


#-------------   Duke Ellington  ------------
plt.subplot(4, 1, 3)
librosa.display.waveplot(duke, alpha=0.5)
plt.ylim((-1, 1))
plt.title("Duke Ellington")

#-------------   piano_c5  ------------
plt.subplot(4, 1, 4)
librosa.display.waveplot(piano_c5, alpha=0.5)
plt.ylim((-1, 1))
plt.title("piano_c5")


plt.show()

#-------------   piano_c5  ------------
plt.subplot(3, 1, 1)
librosa.display.waveplot(piano_c5, alpha=0.5)
plt.ylim((-1, 1))
plt.title("piano_c5")
plt.show()

FRAME_SIZE = 1024
HOP_LENGTH = 512


def amplitude_envelope(signal, frame_size, hop_length):
    """Calculate the amplitude envelope of a signal with a given
    frame size and hop length."""
    amplitude_envelope = []

    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length):
        amplitude_envelope_current_frame = max(signal[i:i + frame_size])
        amplitude_envelope.append(amplitude_envelope_current_frame)

    return np.array(amplitude_envelope)

    
ae_debussy = amplitude_envelope(debussy, FRAME_SIZE, HOP_LENGTH)

print("amplitude_envelope list  = ", ae_debussy)
print("len(ae_debussy) = ",len(ae_debussy))


# calculate amplitude envelope for RHCP and Duke Ellington
ae_redhot = amplitude_envelope(redhot, FRAME_SIZE, HOP_LENGTH)
ae_duke = amplitude_envelope(duke, FRAME_SIZE, HOP_LENGTH)

ae_piano_c5 = amplitude_envelope(piano_c5, FRAME_SIZE, HOP_LENGTH)

# Visualising amplitude envelope
frames = range(len(ae_debussy))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

# amplitude envelope is graphed in red

plt.figure(figsize=(15, 17))

ax = plt.subplot(4, 1, 1)
librosa.display.waveplot(debussy, alpha=0.5)
plt.plot(t, ae_debussy, color="r")
plt.ylim((-1, 1))
plt.title("Debusy")

plt.subplot(4, 1, 2)
librosa.display.waveplot(redhot, alpha=0.5)
plt.plot(t, ae_redhot, color="r")
plt.ylim((-1, 1))
plt.title("RHCP")

plt.subplot(4, 1, 3)
librosa.display.waveplot(duke, alpha=0.5)
plt.plot(t, ae_duke, color="r")
plt.ylim((-1, 1))
plt.title("Duke Ellington")

frames = range(len(ae_piano_c5))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
plt.subplot(4, 1, 4)
librosa.display.waveplot(piano_c5, alpha=0.5)
plt.plot(t,ae_piano_c5, color="r")
plt.ylim((-1, 1))
plt.title("ae_piano_c5")

plt.show()