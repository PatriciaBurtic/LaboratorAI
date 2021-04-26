from math import exp
from numpy.linalg import inv
import numpy as np

def sigmoid(x):
    return 1 / (1 + exp(-x))
    
class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learningRate = 0.001, noEpochs = 1000):
        self.coef_ = [0.0 for _ in range(1 + len(x[0]))]   
        for _ in range(noEpochs):
            for i in range(len(x)): # for each sample from the training data
                ycomputed = sigmoid(self.eval(x[i], self.coef_))     # estimate the output
                crtError = ycomputed - y[i]     # compute the error for the current sample
                for j in range(0, len(x[0])):   # update the coefficients
                    self.coef_[j + 1] = self.coef_[j + 1] - learningRate * crtError * x[i][j]
                self.coef_[0] = self.coef_[0] - learningRate * crtError * 1

        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
 
    def eval(self, xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predictOneSample(self, sampleFeatures):
        coefficients = [self.intercept_] + [c for c in self.coef_]
        computedFloatValue = self.eval(sampleFeatures, coefficients)
        return sigmoid(computedFloatValue)
    


    def predict(self, inTest):
        computedLabels = [self.predictOneSample(sample) for sample in inTest]
        return computedLabels