from utils import loadDataSingleFeature, splitDataSingleFeature
class MySGDRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []
    
    def fit(self,x,y,learningRate = 0.001, noEpochs = 1000):
        self.coef_ = [0.0 for _ in range(len(x[0])+1)]

        for _ in range(noEpochs):
            error = 0
            for i in range(len(x)):
                #Eroarea se calculeaza pentru fiecare exemplu de antrenament
                ycomputed = self.eval(x[i])
                crtError = ycomputed - y[i]
                error += crtError
            MeanError = error/len(x)
            for i in range(len(x)):
                for j in range(0,len(x[0])):
                    #Modelul se updateaza dupa ce toate exemplele de antrenament au fost evaluate (la finalul unei epoci)
                    self.coef_[j] = self.coef_[j] - learningRate * MeanError * x[i][j]
                self.coef_[len(x[0])] = self.coef_[len(x[0])] - learningRate * MeanError * 1

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        yi = self.coef_[-1]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi 
    
    def predict(self, x):
        yComputed = [self.eval(xi) for xi in x]
        return yComputed


if __name__ == "__main__":
    inputs,outputs = loadDataSingleFeature("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab8\\2016.csv",'Economy (GDP per Capita)', 'Happiness Score')
    trainInputs,trainOutputs,validationInputs,validationOutputs = splitDataSingleFeature(inputs,outputs)


    xx = [[x] for x in trainInputs]
    regressor = MySGDRegression()
    regressor.fit(xx,trainOutputs)

    w0,w1 = regressor.intercept_, regressor.coef_[0]
    print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')

    computedTestOutputs = [w0 + w1 * el for el in validationInputs]

    error = 0.0
    for t1, t2 in zip(computedTestOutputs, validationOutputs):
        error += (t1 - t2) ** 2
    error = error / len(validationOutputs)
    print('prediction error (manual): ', error)



