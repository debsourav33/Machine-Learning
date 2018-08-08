import math

class GradientDescent():

    def __init__(self, yes_value):
        self.yes_value= yes_value

    def sigmoid(self,z):
        try:
            power= math.pow(math.e,-1*z)
        except OverflowError:
            power= float('inf')
        return 1/(1+power)

    def costFunction(self,th):
        s=0
        for i in range(self.m):
            s+= self.y[i]* math.log10(self.hypothesis(th,self.x[i])) + (1-self.y[i]) * math.log10(1-self.hypothesis(th,self.x[i]))
        return -1*s/self.m

    def hypothesis(self, th, x):
        s=0
        for k in range(self.n):
            s+= th[k]*x[k]

        return self.sigmoid(s)

    def getConverge(self):
        th = []
        tmp=[]
        flag=0
        for i in range(self.n):
            th.append(0)
            tmp.append(1)
        a = .17

        while True:
            #print(self.costFunction(th))
            for j in range(self.n):
                s = 0

                for i in range(self.m):
                    if(self.y[i]==self.yes_value):
                        tmp_y=1
                    else:
                        tmp_y=0

                    s += (self.hypothesis(th,self.x[i])-tmp_y)* self.x[i][j]

                tmp[j] = th[j] - a / self.m * s

            flag=1
            for j in range(0,self.n):
                if (abs(tmp[j] - th[j]) > 0.0001): #if any theta has not yet converged
                    flag=0

            if(flag==1):
                break

            for i in range(0,self.n):
                th[i]= tmp[i]

        return th

    def fit(self, x, y):
        self.x = x
        self.y = y

        self.m = len(x)
        self.n = len(x[0])
        self.th = self.getConverge()

    def predict(self, x):
        prediction = []
        for i in range(len(x)):
            prediction.append(self.hypothesis(self.th, x[i]))

        return prediction

if __name__ == '__main__':

    x= [[1,1],[1,2],[1,3],[2,1],[2,2],[5,2],[6,1],[6,2],[6,3],[7,1],[7,2],[3,7],[3,8],[4,6],[4,7],[4,8]]
    y= [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]

    test=[[4,3],[0,2],[9,0],[2,11],[13,12]]

    tmp_predict= []
    score= []

    for i in range(len(test)):
        test[i].insert(0,1)
        tmp_predict.append(0)
        score.append(0)

    for i in range(len(x)):  # inserting 1 to make theta and x of equal dimension
        x[i].insert(0, 1)

    myClassifiers = []

    for i in range(1,4):
        myClassifiers.append(GradientDescent(i))

    for i in range (len(myClassifiers)):

        myClassifiers[i].fit(x, y)
        prediction = myClassifiers[i].predict(test)
        print("Probability of type",i+1,":",prediction)

        for k in range(len(prediction)):
            if(prediction[k]>score[k]):
                score[k]= prediction[k]
                tmp_predict[k]= i+1


    print("Predicted Type(s):",tmp_predict)