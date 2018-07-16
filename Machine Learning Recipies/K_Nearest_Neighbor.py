from scipy.spatial import distance
from sklearn import datasets

class scrappyKNN():
    def euc(self,a,b):
        return distance.euclidean(a,b)

    def fit(self,data,label):
        self.data= data
        self.label = label

    def predict(self,test):
        prediction=[]

        for x in test:
            label= self.closest(x)
            prediction.append(label)

        return prediction

    def closest(self,test_x):
        best_index=0;
        best_distance= self.euc(test_x,self.data[0]);

        for i in range(1,len(self.data)):
            dist= self.euc(test_x,self.data[i])

            if(dist<best_distance):
                best_distance=dist
                best_index=i

        return self.label[best_index]



iris= datasets.load_iris()

X= iris.data
Y= iris.target

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

train_data, test_data, train_label, test_label= train_test_split(X,Y,test_size= .5)

my_cfier= scrappyKNN()
my_cfier.fit(train_data, train_label)
prediction= my_cfier.predict(test_data)

accuracy= accuracy_score(prediction,test_label)
print(accuracy)