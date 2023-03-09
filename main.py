from fastapi import FastAPI
from decouple import config
from functions import getFFT

myToken = config("my_token")

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
    fast_fourier = getFFT(myToken, startDate, endDate)
    return {"fourier" : fast_fourier}

@app.get("/start_data={startDate}&end_date={endDate}")
async def fourierDates(startDate, endDate):
    fast_fourier = getFFT(myToken, startDate, endDate)
    return {"fourier" : fast_fourier}



