import numpy as np

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

print('mean', np.mean(ages))
print('median', np.median(ages))
# print('mode', np.mode(ages))
print('std', np.std(ages))
print('var', np.var(ages))
print('90th percentile', np.percentile(ages, 90))
