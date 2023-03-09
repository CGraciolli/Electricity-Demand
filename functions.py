import requests
import json
import numpy as np
from scipy.fft import fft
from decouple import config

def getData(token, startDate, endDate, id=1293):
    """
    recives an authetication token, as well as start and end dates,
    it can also recive the id of the variable we want to retrieve, if none is given it will use 1293,
    the id for the real electricity demand.
    returns the values from the start date to the end date, every hour.
    """ 

    home = "https://api.esios.ree.es/"
    route = f"/indicators/{id}?start_date={startDate}&end_date={endDate}&time_trunc=hour&geo_agg=sum"
    url = home + route
    header = {"Accept": "application/json; application/vnd.esios-api-v1+json",
          "Content-Type": "application/json",
          "x-api-key": f"{token}"}
    responseAPI = requests.get(url, headers=header)
    response = responseAPI.text
    parseJson = json.loads(response)
    indicator = parseJson["indicator"]["values"]
    return indicator

def getList(data, column):
    values = list(map(lambda x: x[column], data))
    return values

def getFFT(myToken, startDate, endDate):
    """
    recives an start date and a end date,
    returns the fast fourier transform associated with the real electricity demand for this interval
    """
    data = getData(myToken, startDate, endDate)
    listValues = getList(data)
    x = np.array(listValues)
    fast_fourier = fft(x)
    return fast_fourier




