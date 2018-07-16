from sklearn import tree
from sklearn.datasets import load_iris

feature= [ [140,1], [130,1], [150,0], [170,0] ]
labels= ["apple","apple","orange","orange"]

clf= tree.DecisionTreeClassifier()

clf= clf.fit(feature,labels)

print(clf.predict([[150,0]]))


