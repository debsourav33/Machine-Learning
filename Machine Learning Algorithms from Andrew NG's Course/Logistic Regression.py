import math

class LogisticRegression():

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
                    s += (self.hypothesis(th,self.x[i])-self.y[i])* self.x[i][j]


                """Regularize theta in range 1 to n"""

                # if(j==0):
                #     tmp[j] = th[j] - a / self.m * s
                # else:
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
        self.m = len(self.x)
        self.n = len(self.x[0])
        self.th = self.getConverge()

    def predict(self, x):
        prediction = []
        for i in range(len(x)):
            x[i].insert(0,1)
            prediction.append(self.hypothesis(self.th, x[i]))
        print(self.th)
        return prediction

def getRound(nums):
    res=[]
    for num in nums:
        x= (int) (num)
        rem= abs(num-x)
        if rem>=.5:
            try:
                x+= abs(x)/x #decrement if num is -ve and increment if num is +ve
            except ZeroDivisionError:
                x=x

        res.append(x)

    return res

if __name__ == '__main__':
    myClassifier = LogisticRegression()

    x = [[1,2], [2,1], [1.995,1], [1,1.995], [.923,2], [1,3], [2,2], [0,1], [1.4,1.7]]
    y = [1, 1, 0, 0, 0, 1, 1, 0, 1]

    #x = [[1],[-2],[3],[-1],[-3],[0],[-.05],[-.6]]
    #y = [1,0,1,0,0,1,0,0]

    for i in range(len(x)):  # inserting 1 to make theta and x of equal dimension
        x[i].insert(0, 1)

    myClassifier.fit(x, y)
    test= [[1,2], [2,1], [1.995,1], [1,1.995], [.923,2], [1,3], [2,2], [0,1], [1.4,1.7]]
    prediction = myClassifier.predict(test)

    print(prediction)

    for i in range(len(prediction)):
        if prediction[i]>=.5:
            prediction[i]=1
        else:
            prediction[i]=0

    print("Rounded", prediction)

