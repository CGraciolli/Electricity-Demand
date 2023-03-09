import requests
import json
from decouple import config

def getData(token, startDate, endDate, id=1293):
    """
    recives an authetication token, as well as start and end dates
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

##make it one function
def getList(data):
    values = []
    for datum in data:
        values.append(datum["value"])
    return values

def getListHours(data):
    hours = []
    for datum in data:
        hours.append(datum["datetime"])
    return hours




