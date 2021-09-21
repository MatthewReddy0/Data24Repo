import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

data_frame = pandas.read_csv("shows.csv")

# Making the non-numeric data numeric
data = {'UK': 0, 'USA': 1, 'N': 2}
data_frame['Nationality'] = data_frame['Nationality'].map(data)
data = {'YES': 1, 'NO': 0}
data_frame['Go'] = data_frame['Go'].map(data)

# Separating the feature and target columns
features = ['Age', 'Experience', 'Rank', 'Nationality']
features_X = data_frame[features]
target_Y = data_frame['Go']

# Create a Decision Tree, save it as an image, and show the image:
dtree = DecisionTreeClassifier()
dtree = dtree.fit(features_X, target_Y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

"""
Rank <= 6.5 means that every comedian with a rank of 6.5 or lower will follow the True arrow (to the left), and the rest
 will follow the False arrow (to the right).

gini = 0.497 refers to the quality of the split, and is always a number between 0.0 and 0.5, where 0.0 would mean all of
 the samples got the same result, and 0.5 would mean that the split is done exactly in the middle.

samples = 13 means that there are 13 comedians left at this point in the decision, which is all of them since this is
 the first step.

value = [6, 7] means that of these 13 comedians, 6 will get a "NO", and 7 will get a "GO".
"""

# Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of
# 7?
print(dtree.predict([[40, 10, 7, 1]]))
