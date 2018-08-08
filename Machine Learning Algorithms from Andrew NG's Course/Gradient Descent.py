class GradientDescent():

    def hypothesis(self, th0, th1, x):
        return th0 + th1 * x

    def getConverge(self):
        th0 = 0
        th1 = 0
        a = .3

        while True:

            s = 0
            for i in range(self.m):
                s += self.hypothesis(th0, th1, self.x[i]) - self.y[i]
            print("Hypo: " + str(s / self.m))
            tmp0 = th0 - a / self.m * s

            s = 0
            for i in range(self.m):
                s += (self.hypothesis(th0, th1, self.x[i]) - self.y[i]) * self.x[i]
            tmp1 = th1 - a / self.m * s

            if (tmp0 == th0 or tmp1 == th1):
                break

            th0 = tmp0
            th1 = tmp1

        return th0, th1

    def fit(self, x, y):
        self.x = x
        self.y = y
        self.m = len(x)
        self.th0, self.th1 = self.getConverge()

    def predict(self, test):
        predictions = []

        for x in test:
            predictions.append(self.hypothesis(self.th0, self.th1, x))

        return predictions


if __name__ == '__main__':
    myLinearRegressor = GradientDescent()

    x = [1, 2, 3]
    y = [8, 13, 18]

    test=[1,2.5,7]

    myLinearRegressor.fit(x, y)
    print("\nPrediction: ", myLinearRegressor.predict(test))
