import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.random.uniform(0.0, 5.0, 250)
# x = np.random.normal(5.0, 1.0, 100000)
print('random.uniform')
plt.hist(x, 5)
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def line_function(x):
    return slope * x + intercept


linear_model = list(map(line_function, x))

plt.scatter(x, y)
plt.plot(x, linear_model)
plt.show()
print(f'r:{r} \np:{p} \nstd_err:{std_err} \nfuture value:{line_function(10)}')
