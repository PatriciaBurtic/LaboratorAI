import csv
import matplotlib.image as mpimg
import numpy as np

from sklearn.preprocessing import StandardScaler

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

def loadData(filename):
    data = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                data.append(row)
            line_count += 1
        
    inputs = [toGrayscale(mpimg.imread('imgs\\'+data[i][0])) for i in range(len(data))]
    outputs = [int(data[i][1]) for i in range(len(data))]

    return inputs,outputs

def toGrayscale(mat):
    x = []
    for line in mat:
        y=[]
        for pixel in line:
            y.append(sum(pixel)//3)
        x.append(y)
    return x 

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

def flatten(mat):
    x = []
    for line in mat:
        for el in line:
            x.append(el)
    return x 

    
