import requests
import json
from decouple import config

def getData(token, startDate, endDate, id):
    """
    recives an authetication token, as well as start and end dates
    """ 

    home = "https://api.esios.ree.es/"
    route = f"/indicators/{id}?start_date={startDate}&end_date={endDate}&date_type=datos&time_trunc=hour&geo_agg=sum"
    url = home + route
    header = {"Accept": "application/json; application/vnd.esios-api-v1+json",
          "Content-Type": "application/json",
          "x-api-key": f"{token}"}
    responseAPI = requests.get(url, headers=header)
    response = responseAPI.text
    parseJson = json.loads(response)
    return parseJson


startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")
id = 1293

data = getData(myToken, startDate, endDate, id)
for d in data:
    print(d["value"])
    print(d["datetime"])



