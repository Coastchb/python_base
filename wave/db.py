import matplotlib.pyplot as plt
import librosa
from librosa import display
import numpy as np
y, sr = librosa.load("10000.wav", sr=16000)
y_db = librosa.amplitude_to_db(y, ref=np.max)

plt.subplot(2,1,1)
display.waveplot(y, sr = 16000)
plt.subplot(2,1,2)
display.waveplot(y_db, sr = 16000)

plt.show();

'''
y_filt = librosa.effects.preemphasis(y)
# and plot the results for comparison
S_orig = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
S_preemph = librosa.amplitude_to_db(np.abs(librosa.stft(y_filt)), ref=np.max)
plt.subplot(2,1,1)
librosa.display.specshow(S_orig, y_axis='log', x_axis='time')
plt.title('Original signal')
plt.colorbar()
plt.subplot(2,1,2)
display.specshow(S_preemph, y_axis='log', x_axis='time')
plt.title('Pre-emphasized signal')
plt.colorbar()
plt.tight_layout();
plt.show();
'''
