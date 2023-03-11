from seaborn import pointplot
import matplotlib.pyplot as plt
from functions import getList, getData
from decouple import config
from scipy.signal import welch


startDate = "2018-09-02T00:00:00+00:00"
endDate = "2018-10-06T23:59:59+00:00"
myToken = config("my_token")
data = getData(myToken, startDate, endDate)
listHours = getList(data, "datetime")
listValues = getList(data, "value")
listLabels = []
for index, time in enumerate(listHours):
    if index % 24 == 0:
        day = time[8:10]
        month = time[5:7]
        listLabels.append(f"{month}/{day}")
    else:
        listLabels.append(time)
ax = pointplot(x=listLabels, y=listValues)
for i, label in enumerate(ax.get_xticklabels()):
        if i % 24 != 0:
            label.set_visible(False)
plt.title("Real Electricity Demand in Spain", fontsize=20)
plt.ylabel("Real Demand in MW")
plt.xticks(rotation = 90)
plt.show()

##periodogram
f, pxx = welch(listValues)
plt.ylabel("Real Demand")
plt.xlabel("Frequency")
plt.plot(f, pxx)
plt.title("Periodogram for the Real Demand Electricity in Spain", fontsize=20)
plt.show()
