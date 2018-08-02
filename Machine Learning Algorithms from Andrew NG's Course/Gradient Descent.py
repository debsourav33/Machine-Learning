class GradientDescent():
    def hypothesis(self,th0,th1,x):
        return th0+th1*x

    def getConverge(self):
        th0=0
        th1=0
        a= .17

        while True:
            s= 0
            for i in range(self.m):
                s+= self.hypothesis(th0,th1,self.x[i])-self.y[i]
            tmp0= th0- a/self.m*s

            s= 0
            for i in range(self.m):
                s+= (self.hypothesis(th0,th1,self.x[i])-self.y[i])*self.x[i]
            tmp1= th1- a/self.m*s

            if (tmp0==th0 or tmp1==th1):
                break

            th0= tmp0
            th1= tmp1

        return th0, th1

    def fit(self,x,y):
        self.x=x
        self.y=y
        self.m=len(x)
        self.th0, self.th1= self.getConverge()

    def predict(self,x):
        return self.hypothesis(self.th0,self.th1,x)


if __name__ == '__main__':
    myClassifier= GradientDescent()

    x=[1,2,3]
    y=[2,-3,-7]

    myClassifier.fit(x,y)
    print(myClassifier.predict(4))



