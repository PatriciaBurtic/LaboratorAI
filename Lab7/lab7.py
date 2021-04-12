from utils import showPlots,loadData
import numpy as np 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 
from myLinearRegression import MyLinearUnivariateRegression

def splitData(inputs,outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(outputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(outputs)), replace = False)
    validationSample = [i for i in indexes  if not i in trainSample]

    trainInputs1 = [inputs[0][i] for i in trainSample]
    trainInputs2 = [inputs[1][i] for i in trainSample]

    trainInputs = [trainInputs1,trainInputs2]

    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs1 = [inputs[0][i] for i in validationSample]
    validationInputs2 = [inputs[1][i] for i in validationSample]

    validationInputs = [validationInputs1,validationInputs2]

    validationOutputs = [outputs[i] for i in validationSample]

    return trainInputs,trainOutputs,validationInputs,validationOutputs



if __name__=="__main__":

    #load data
    inputs, outputs = loadData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab7\\2016.csv", 'Economy (GDP per Capita)','Freedom', 'Happiness Score')
    
    #show data, check the linearity
    showPlots(inputs,outputs)

    #split the data in training data and validation data
    trainInputs,trainOutputs,validationInputs,validationOutputs = splitData(inputs,outputs)

    #plot the train and validation data

    ax = plt.axes(projection='3d')
    ax.scatter3D(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='Blues',label="Training data")
    ax.scatter3D(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Reds',label="Validation data")
    plt.title('train and validation data')
    plt.xlabel('GDP capita')
    plt.ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.legend()
    plt.show()



    #plot the learnt model
    # prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
    noOfPoints = 1000
    xref = []
    val = min(trainInputs[0])
    step = (max(trainInputs[0]) - min(trainInputs[0])) / noOfPoints
    for i in range(1, noOfPoints):
        xref.append(val)
        val += step

    yref = []
    val = min(trainInputs[1])
    step = (max(trainInputs[1]) - min(trainInputs[1])) / noOfPoints
    for i in range(1, noOfPoints):
        yref.append(val)
        val += step

    #learning step
    
    regressor = linear_model.LinearRegression()
    # training the model by using the training inputs and known training outputs
    xx = [[el1,el2] for el1,el2 in zip(trainInputs[0],trainInputs[1])]
    regressor.fit(xx, trainOutputs)
    # save the model parameters
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    print('the learnt model (tool): f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')


    # regressor = MyLinearUnivariateRegression()
    # regressor.fit(trainInputs[0],trainInputs[1], trainOutputs)
    # # save the model parameters
    # w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    # print('the learnt model (code) : f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')
    
    zref = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(xref,yref)]

    ax = plt.axes(projection='3d')
    ax.scatter3D(xref, yref, zref, c=zref, cmap='Blues',label="Learnt model")
    ax.scatter3D(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='Reds',label="Training data")
    plt.title('train data and the learnt model')
    plt.xlabel('GDP capita')
    plt.ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.legend()
    plt.show()



    # use the trained model to predict new inputs

    computedValidationOutputs  = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(validationInputs[0],validationInputs[1])]

            # plot the computed outputs (see how far they are from the real outputs)
    ax = plt.axes(projection='3d')
    ax.scatter3D(validationInputs[0], validationInputs[1], computedValidationOutputs, c=computedValidationOutputs, cmap='Blues',label="Computed")
    ax.scatter3D(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Reds',label="Real test data")
    plt.title('computed validation and real validation data')
    plt.xlabel('GDP capita')
    plt.ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.legend()
    plt.show()


    #compute the differences between the predictions and real outputs
    
    error = 0.0
    for t1, t2 in zip(computedValidationOutputs, validationOutputs):
        error += (t1 - t2) ** 2
    error = error / len(validationOutputs)
    print("prediction error (manual): ", error)


    error = mean_squared_error(validationOutputs, computedValidationOutputs)
    print('Prediction error (tool):  ', error)