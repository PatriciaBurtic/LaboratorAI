import csv
import numpy as np
from sklearn.preprocessing import StandardScaler
import random
import math

def loadData(fileName):
    inputs = []
    outputs = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader: 
            inputs.append([float(row[0]),float(row[1]),float(row[2]),float(row[3])])
            outputs.append(row[4])
    
    return inputs, outputs

def splitData(inputs,outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(outputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(outputs)), replace = False)
    validationSample = [i for i in indexes  if not i in trainSample]


    trainInputs = [inputs[i] for i in trainSample]

    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]

    return trainInputs,trainOutputs,validationInputs,validationOutputs

def mySplitData(inputs,outputs):
    indexes = [i for i in range(len(outputs))]
    trainSample = []
    for i in range(0,int(0.8*len(inputs))+1):
        nr = random.randint(0,len(inputs)-1)
        if nr not in trainSample:
            trainSample.append(nr)
    validationSample = [i for i in indexes  if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]

    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]

    return trainInputs,trainOutputs,validationInputs,validationOutputs


def normalisation(trainData, testData):
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]
        
        scaler.fit(trainData) 
        normalisedTrainData = scaler.transform(trainData)
        normalisedTestData = scaler.transform(testData) 
        
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData) 
        normalisedTrainData = scaler.transform(trainData)
        normalisedTestData = scaler.transform(testData)  
    return normalisedTrainData, normalisedTestData

def myNormalisation(trainInputs, validationInputs):
    trainInputsNorm = []
    for i in range(len(trainInputs)):
        trainInputsNorm.append([math.log(trainInputs[i][0]),math.log(trainInputs[i][1]),math.log(trainInputs[i][2]),math.log(trainInputs[i][3])])

    validationInputsNorm = []
    for i in range(len(validationInputs)):
        validationInputsNorm.append([math.log(validationInputs[i][0]),math.log(validationInputs[i][1]),math.log(validationInputs[i][2]),math.log(validationInputs[i][3])])

    return trainInputsNorm,validationInputsNorm
   

def transform(outputs):
    transformed = []
    for i in range(len(outputs)):
        if(outputs[i]=='Iris-virginica'):
            transformed.append(2)
        if(outputs[i]=='Iris-versicolor'):
            transformed.append(1)
        if(outputs[i]=='Iris-setosa'):
            transformed.append(0)
    return transformed
