from seaborn import pointplot
import matplotlib.pyplot as plt
from functions import getList, getData
from decouple import config

startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")
data = getData(myToken, startDate, endDate)
listHours = getList(data, "datetime")
listValues = getList(data, "value")

##x axis markings missing
pointplot(x=listHours, y=listValues)
plt.ylabel("Real Demand")
plt.xlabel("Time")
plt.xticks([])
plt.show()
