from fastapi import FastAPI
from decouple import config
from functions import jsonFFT

myToken = config("my_token")
app = FastAPI()

@app.get("/")
async def fourier():
    """
    retrieves data for the real electricity demand from September 2nd to October 10th of 2018 from an API
    returns a json format with the fast fourier transform, divided in two lists,
    one for the real part of the numbers, the other for the imaginary parts
    """
    startDate = "2018-09-02T00:00:00+00:00"
    endDate = "2018-10-06T23:59:59+00:00"
    jsonFourier = jsonFFT(myToken, startDate, endDate)
    return jsonFourier

@app.get("/start_date={startDate}&end_date={endDate}")
async def fourierDates(startDate, endDate):
    """
    retrieves  data for the real electricity demand from the start date to the end date from an API
    returns a json format with the fast fourier transform, divided in two lists,
    one for the real part of the numbers, the other for the imaginary parts
    """
    jsonFourier = jsonFFT(myToken, startDate, endDate)
    return jsonFourier



