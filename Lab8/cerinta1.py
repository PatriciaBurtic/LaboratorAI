from utils import loadData,splitData
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    inputs,outputs = loadData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab8\\2016.csv",'Economy (GDP per Capita)','Freedom', 'Happiness Score')
    trainInputs,trainOutputs,validationInputs,validationOutputs = splitData(inputs,outputs)

    xx = [[el1,el2] for el1,el2 in zip(trainInputs[0],trainInputs[1])]
    regressor = linear_model.SGDRegressor(alpha=0.01,max_iter=100)
    for _ in range(1000):
        regressor.partial_fit(xx,trainOutputs)
    w0, w1, w2 = regressor.intercept_[0],regressor.coef_[0],regressor.coef_[1]

    print('the learnt model (tool): f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

    computedTestOutputs = regressor.predict([[el1,el2] for el1,el2 in zip(validationInputs[0],validationInputs[1])])

    error = mean_squared_error(validationOutputs, computedTestOutputs)
    print('prediction error (tool):  ', error)





