import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def line_function(x):
    return slope * x + intercept


flights = sns.load_dataset('flights')
print(flights.head())
flights_wide = flights.pivot("year", "month", "passengers")

sns.lineplot(data=flights_wide)
plt.title('Passenger numbers across time')
plt.xlabel('Year')
plt.ylabel('Number of passengers')
plt.show()


"""
Second Graph
"""

col_list = ["year", "month", "passengers"]
df = pd.read_csv("flights.csv", usecols=col_list)

# x = np.arange([1949, 1961, 1/12])
x = range(0, 144)
y = df['passengers']
plt.title('Passenger numbers across time')
plt.xlabel('Year')
plt.ylabel('Number of passengers')
plt.scatter(x, y)

slope, intercept, r, p, std_err = stats.linregress(x, y)
linear_model = list(map(line_function, x))

plt.plot(x, linear_model)
print(f'r:{r} \np:{p} \nstd_err:{std_err} \nfuture value:{line_function(10)}')
plt.show()
