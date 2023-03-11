from fastapi import FastAPI
from decouple import config
from scipy.signal import welch
from functions import getData, getList

myToken = config("my_token")

app = FastAPI()

## the apis should return json format
@app.get("/")
async def getwelch():
    """
    retrieves  data for the real electricity demand from September 2nd to October 10th of 2018 from an API
    returns the power spectral density
    """
    startDate = "2018-09-02T00:00:00+00:00"
    endDate = "2018-10-06T23:59:59+00:00"
    data = getData(myToken, startDate, endDate)
    listValues = getList(data, "value")
    f, pxx = welch(listValues)
    return {"f" : f, "pxx": pxx}

@app.get("/start_date={startDate}&end_date={endDate}")
async def welchDates(startDate, endDate):
    """
    retrieves  data for the real electricity demand from the start date to the end date from an API
    returns the power spectral density
    """
    data = getData(myToken, startDate, endDate)
    listValues = getList(data, "value")
    f, pxx = welch(listValues)
    return {"f" : f, "pxx": pxx}
