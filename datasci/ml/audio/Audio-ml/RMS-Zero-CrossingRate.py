"""
Basic processing operations on audio with Librosa

Load audio files, visualise waveform.
How to extract Root-Mean Square Energy (RMSE) and
Zero-Crossing Rate (ZCR) from audio data using the Python library
librosa.
I also show how RMS and ZCR vary depending on music genre and type
of audio source (i.e., voice vs noise).

https://librosa.org/doc/latest/index.html

Sound classification with YAMNet
https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/yamnet.ipynb?skip_cache=true#scrollTo=Wo9KJb-5zuz1
https://drive.google.com/drive/my-drive

https://www.youtube.com/watch?v=EycaSbIRx-0&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=10
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

# ipd.Audio(debussy_file)
# load audio files with librosa

debussy, sr = librosa.load(debussy_file)
redhot, _ = librosa.load(redhot_file)
duke, _ = librosa.load(duke_file)

# Root-mean-squared energy with Librosa
FRAME_SIZE = 1024
HOP_LENGTH = 512

rms_debussy = librosa.feature.rms(debussy, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
rms_redhot = librosa.feature.rms(redhot, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
rms_duke = librosa.feature.rms(duke, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]

# Returns  rmsnp.ndarray [shape=(1, t)]  RMS value for each frame

print("len(rms_debussy) = ", len(rms_debussy))
print("rms_debussy.shape ", rms_debussy.shape)
print("RMS value for each frame in  debussy wav file \n ", rms_debussy)

# Visualise RMSE + waveform
frames = range(len(rms_debussy))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
"""
librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
Returns
     timesnp.ndarray [shape=(n,)]
     time (in seconds) of each given frame number:
     times[i] = frames[i] * hop_length / sr
"""
# rms energy is graphed in red

plt.figure(figsize=(15, 17))

ax = plt.subplot(3, 1, 1)
librosa.display.waveplot(debussy, alpha=0.5)
plt.plot(t, rms_debussy, color="r")
plt.ylim((-1, 1))
plt.title("Debusy")

plt.subplot(3, 1, 2)
librosa.display.waveplot(redhot, alpha=0.5)
plt.plot(t, rms_redhot, color="r")
plt.ylim((-1, 1))
plt.title("RHCP")

plt.subplot(3, 1, 3)
librosa.display.waveplot(duke, alpha=0.5)
plt.plot(t, rms_duke, color="r")
plt.ylim((-1, 1))
plt.title("Duke Ellington")

plt.show()  # 7:04

'''
The next  function is  doing the same RMS  calculatio but
wuthout  using the inbuild librosa  function (ibrosa.feature.rms)


'''


def rmse(signal, frame_size, hop_length):
    rmse = []

    # calculate rmse for each frame
    for i in range(0, len(signal), hop_length):
        rmse_current_frame = np.sqrt(sum(signal[i:i + frame_size] ** 2) / frame_size)
        rmse.append(rmse_current_frame)  # Add to  rms list
    return np.array(rmse)  # convert to np array


# Use  our  homemade rms function
rms_debussy1 = rmse(debussy, FRAME_SIZE, HOP_LENGTH)
rms_redhot1 = rmse(redhot, FRAME_SIZE, HOP_LENGTH)
rms_duke1 = rmse(duke, FRAME_SIZE, HOP_LENGTH)
# Draw  our  homemade rms function and the lebrose function on
# the same  graph

plt.figure(figsize=(15, 17))

ax = plt.subplot(3, 1, 1)
librosa.display.waveplot(debussy, alpha=0.5)
plt.plot(t, rms_debussy, color="r")
plt.plot(t, rms_debussy1, color="y")
plt.ylim((-1, 1))
plt.title("Debusy")

plt.subplot(3, 1, 2)
librosa.display.waveplot(redhot, alpha=0.5)
plt.plot(t, rms_redhot, color="r")
plt.plot(t, rms_redhot1, color="y")
plt.ylim((-1, 1))
plt.title("RHCP")

plt.subplot(3, 1, 3)
librosa.display.waveplot(duke, alpha=0.5)
plt.plot(t, rms_duke, color="r")
plt.plot(t, rms_duke1, color="y")
plt.ylim((-1, 1))
plt.title("Duke Ellington")

plt.show()

''' 
Zero - crossing rate with Librosa   18:
librosa.org/doc/latest/feature.html#spectral-features
librosa.org/doc/latest/generated/librosa.feature.zero_crossing_rate.html#librosa.feature.zero_crossing_rate

librosa.feature.zero_crossing_rate :  
  Returns  zcrnp.ndarray  [shape=(1, t)]
  zcr[0, i] is the fraction of zero crossings in the ith frame
'''
zcr_debussy = librosa.feature.zero_crossing_rate(debussy, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
zcr_redhot = librosa.feature.zero_crossing_rate(redhot, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
zcr_duke = librosa.feature.zero_crossing_rate(duke, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]

print("zcr_debussy.size", zcr_debussy.size)
print("zcr_debussy ", zcr_debussy)

plt.figure(figsize=(15, 10))

plt.plot(t, zcr_debussy, color="y")
plt.plot(t, zcr_redhot, color="r")
plt.plot(t, zcr_duke, color="b")
plt.ylim(0, 1)
plt.show()

# non normalize zcr.  The y aix numbers are the  real zcr
plt.figure(figsize=(15, 10))

plt.plot(t, zcr_debussy * FRAME_SIZE, color="y")
plt.plot(t, zcr_redhot * FRAME_SIZE, color="r")
plt.plot(t, zcr_duke * FRAME_SIZE, color="b")

plt.ylim(0, 500)
plt.show()

## ZCR: Voice vs Noise  24:00

voice_file = os.path.join(BASE_FOLDER, "voice.wav")
noise_file = os.path.join(BASE_FOLDER, "noise.wav")

DURATION = 15
voice, _ = librosa.load(voice_file, duration=DURATION)
noise, _ = librosa.load(noise_file, duration=DURATION)

# get ZCR
zcr_voice = librosa.feature.zero_crossing_rate(voice, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
zcr_noise = librosa.feature.zero_crossing_rate(noise, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
frames = range(len(zcr_voice))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

plt.figure(figsize=(15, 10))
plt.title("Voice vs Noise - voice:yellow noise:red ")
plt.plot(t, zcr_voice, color="y")
plt.plot(t, zcr_noise, color="r")
plt.ylim(0, 1)
plt.show()
