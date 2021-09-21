import numpy as np
import matplotlib.pyplot as plt
import pandas
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

poly_model = np.poly1d(np.polyfit(x, y, 3))
poly_line = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(poly_line, poly_model(poly_line))
plt.show()
print(r2_score(y, poly_model(x)))
print(f'future value: {poly_model(17)}')


"""
Multiple regression AND Scaling
"""
scale = StandardScaler()
data_frame = pandas.read_csv("cars2.csv")

X = data_frame[['Weight', 'Volume']]
y = data_frame['CO2']

scaledX = scale.fit_transform(X)

regression = linear_model.LinearRegression()
regression.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regression.predict([scaled[0]])
print(f'predictedCO2: {predictedCO2}')
