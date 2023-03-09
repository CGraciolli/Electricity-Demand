from fastapi import FastAPI
from decouple import config
import numpy as np
from scipy.fft import fft
from data import getData, getList

app = FastAPI()

@app.get("/")
##not sure about the async
async def fourier():
    """
    retrieves  data for the real electricity demand from September 2nd to October 10th of 2018 from an API
    returns the Fast Fourier Transform
    """
    startDate = "2018-09-02T00:00:00+00:00"
    endDate = "2018-10-06T23:59:59+00:00"
    myToken = config("my_token")
    data = getData(myToken, startDate, endDate)
    listValues = getList(data)
    x = np.array(listValues)
    fast_fourier = fft(x)
    return {"fourier" : fast_fourier}

@app.get("/start_data={startDate}&end_date={endDate}")
async def fourierDates(startDate, endDate):
    myToken = config("my_token")
    data = getData(myToken, startDate, endDate)
    listValues = getList(data)
    x = np.array(listValues)
    fast_fourier = fft(x)
    return {"fourier" : fast_fourier}

##the repeated part could be a separate function

