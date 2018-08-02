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
        a = .17
        cnt=0
        while True:
            cnt+=1
            #print(cnt)
            for j in range(self.n):
                s = 0
                for i in range(self.m):
                    s += (self.hypothesis(th,self.x[i])-self.y[i])* self.x[i][j]

                tmp[j] = th[j] - a / self.m * s

            for j in range(self.n):
                flag=1
                if (tmp[j] != th[j]): #if any of the thetas has not yet converged
                    flag=0

            if(flag==1):
                break

            for i in range(self.n):
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

        return prediction


if __name__ == '__main__':
    myClassifier = GradientDescent()

    x = [[0,1, 2], [2,2, 2]]
    y = [4, 8]

    for i in range(len(x)): #inserting 1 to make theta and x of equal dimension
        x[i].insert(0,1)

    myClassifier.fit(x, y)
    test=[[1,2,3]]
    print(myClassifier.predict(test))

