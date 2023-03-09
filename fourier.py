from scipy.fft import fft
from scipy.signal import periodogram, welch
import numpy as np
import matplotlib.pyplot as plt
from decouple import config
from functions import getData, getList

##delete this file after I understand the periodogram,
##everything should be in fucntions
startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")

data = getData(myToken, startDate, endDate)
listValues = getList(data, "value")

x = np.array(listValues)
fast_fourier = fft(x)

f, pxx = welch(x)
plt.semilogy(f, pxx)
plt.show()
