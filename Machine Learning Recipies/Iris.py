from sklearn.datasets import load_iris
from sklearn import tree
import numpy

iris= load_iris()

print (iris.feature_names)
print (iris.target_names)


test_idx= [0,50,100]

train_target= numpy.delete(iris.target, test_idx)
train_data= numpy.delete(iris.data, test_idx, axis=0)


clf= tree.DecisionTreeClassifier()

clf= clf.fit(train_data, train_target)

test_data= iris.data[test_idx]
test_target= iris.target[test_idx]

print (test_target)
print (test_data[0])


print (clf.predict(test_data))

new_data= [5.2, 3.4, 1.5, 0.3]


print (clf.predict([new_data]))
