from cerinta2 import MySGDRegression
from utils import loadData, mySplitData,dataNormalisation, splitData
import math

if __name__ == "__main__":
    inputs,outputs = loadData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab8\\2016.csv",'Economy (GDP per Capita)','Freedom', 'Happiness Score')
    trainInputs,trainOutputs,validationInputs,validationOutputs = mySplitData(inputs,outputs)

    xx = [[el1,el2] for el1,el2 in zip(trainInputs[0],trainInputs[1])]
    regressor = MySGDRegression()
    regressor.fit(xx,trainOutputs)
    w0, w1, w2 = regressor.intercept_,regressor.coef_[0],regressor.coef_[1]

    print('the learnt model (tool): f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

    computedTestOutputs = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(validationInputs[0],validationInputs[1])]

    error = 0.0
    for t1, t2 in zip(computedTestOutputs, validationOutputs):
        error += (t1 - t2) ** 2
    error = error / len(validationOutputs)
    print('prediction error (manual): ', error)

    trainInputsNorm, validationInputsNorm = dataNormalisation(trainInputs,validationInputs)
    print("NORM: ",trainInputsNorm)
