import librosa
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio, display
import pandas as pd
from scipy.spatial.distance import euclidean




# Load the audio file
music, sr = librosa.load('data/testAudio.mp3', sr=None, mono=True,offset= 81, duration=60)

# Extract features
librosa.display.waveshow(music, sr=sr)
plt.title('Waveform of the Audio')
plt.xlabel('Time m:ss')
plt.show()
