from scipy.fft import rfft, rfftfreq
import numpy as np
import matplotlib.pyplot as plt
from decouple import config
from functions import getData, getList

##delete this file after I understand the periodogram,
##everything should be in functions
startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")

data = getData(myToken, startDate, endDate)
listValues = getList(data, "value")

##the key to getting the sample rate and the duration should be figuring out the x axis

#N = SAMPLE_RATE * DURATION
x = np.array(listValues)
##we use the real fat fourier transform instead of fft followed by np.abs for time efficiency
yf = rfft(x)
#xf = rfftfreq(N, 1/SAMPLE_RATE)
#plt.plot(xf, yf))
#plt.show()

