from scipy.fft import fft
from scipy.signal import periodogram
import numpy as np
import matplotlib.pyplot as plt
from data import listValues

x = np.array(listValues)
fast_fourier = fft(x)

