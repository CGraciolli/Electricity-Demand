from seaborn import pointplot
import matplotlib.pyplot as plt
from data import listValues, listHours

pointplot(x=listHours, y=listValues)
plt.show()
