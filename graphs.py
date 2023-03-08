from seaborn import pointplot
import matplotlib.pyplot as plt
from data import listValues, listHours

##x axis markings missing
pointplot(x=listHours, y=listValues)
plt.ylabel("Real Demand")
plt.xlabel("Time")
plt.xticks([])
plt.show()
