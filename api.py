import requests
from decouple import config

def getData(token, startDate, endDate, id):
    """
    recives an authetication token, as well as start and end dates, and the data id
    returns a json with the data 
    """ 

    home = "https://api.esios.ree.es/"
    ##not sure about the id
    route = f" /indicators?start_date={startDate}&end_date={endDate}&taxonomy_ids[]={id}"
    url = home + route
    header = {"Accept": "application/json; application/vnd.esios-api-v1+json",
          "Content-Type": "application/json",
          "x-api-key": f"{token}"}
    response = requests.get(url, headers=header)
    json = response.json()
    return json

startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")
variable = "Demanda Real"
id = 1293

data = getData(myToken, startDate, endDate, id)
print(data)
