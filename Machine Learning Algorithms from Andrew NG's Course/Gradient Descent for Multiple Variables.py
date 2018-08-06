class GradientDescent():
    def hypothesis(self, th, x):
        s=0
        for i in range(self.n):
            s+= th[i]*x[i]

        return s

    def getConverge(self):
        th = []
        tmp=[]
        flag=0
        for i in range(self.n):
            th.append(0)
            tmp.append(1)
        a = .017
        while True:

            for j in range(self.n):
                s = 0
                for i in range(self.m):
                    s += (self.hypothesis(th,self.x[i])-self.y[i])* self.x[i][j]

                print("Hypo: " + str(s / self.m))
                tmp[j] = th[j] - a / self.m * s

            flag=1
            for j in range(0,self.n):
                if (tmp[j] != th[j]): #if any theta has not yet converged
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
            x+= abs(x)/x #decrement if num is -ve and increment if num is +ve
        res.append(x)

    return res


if __name__ == '__main__':
    myClassifier = GradientDescent()

    x = [[-2,-1],[1,1],[1,-2],[0,0],[3,0],[2,4]]
    y = [-3,-1,5,-1,5,-5]

    for i in range(len(x)): #inserting 1 to make theta and x of equal dimension
        x[i].insert(0,1)

    myClassifier.fit(x, y)
    test=[[4,1]]
    prediction= myClassifier.predict(test)

    print(prediction)
    print("Rounded:",int(getRound(prediction)[0]))

