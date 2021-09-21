import numpy

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

"""
The first 80% of the data is the training data
The last 20% of the data is the testing data

Higher r2_score() means it's a better model
"""