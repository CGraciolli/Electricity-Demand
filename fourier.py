from scipy.fft import fft
from scipy.signal import periodogram
import numpy as np
import matplotlib.pyplot as plt
from data import listValues
from seaborn import pointplot

x = np.array(listValues)
fast_fourier = fft(x)

f, pxx = periodogram(x)
plt.semilogy(f, pxx)
plt.show()
