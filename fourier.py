from fastapi import FastAPI
from decouple import config
from functions import getFFT
import json

myToken = config("my_token")

app = FastAPI()

## the apis should return json format
@app.get("/")
async def fourier():
    """
    retrieves data for the real electricity demand from September 2nd to October 10th of 2018 from an API
    returns the Fast Fourier Transform
    """
    startDate = "2018-09-02T00:00:00+00:00"
    endDate = "2018-10-06T23:59:59+00:00"
    fast_fourier = list(getFFT(myToken, startDate, endDate))
    return json.dumps(fast_fourier)

@app.get("/start_date={startDate}&end_date={endDate}")
async def fourierDates(startDate, endDate):
    """
    retrieves  data for the real electricity demand from the start date to the end date from an API
    returns the Fast Fourier Transform
    """
    fast_fourier = getFFT(myToken, startDate, endDate)
    return {"fourier" : fast_fourier}



