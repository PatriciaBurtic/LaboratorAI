import numpy as np
import csv
import random 
import math


def loadData(fileName, inputVariabName1, inputVariabName2, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable1 = dataNames.index(inputVariabName1)
    selectedVariable2 = dataNames.index(inputVariabName2)
    inputs1 = [float(data[i][selectedVariable1]) for i in range(len(data))]
    inputs2 = [float(data[i][selectedVariable2]) for i in range(len(data))]
    inputs=[inputs1,inputs2]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

def loadDataSingleFeature(fileName, inputVariabName1, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable1 = dataNames.index(inputVariabName1)
    inputs = [float(data[i][selectedVariable1]) for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

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

def splitDataSingleFeature(inputs,outputs):
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


def mySplitData(inputs,outputs):
    indexes = [i for i in range(len(outputs))]
    trainSample = []
    for i in range(0,int(0.8*len(inputs[0]))+1):
        nr = random.randint(0,len(inputs[0])-1)
        if nr not in trainSample:
            trainSample.append(nr)
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


def dataNormalisation(trainInputs,validationInputs):
    trainInputsNorm = [[math.log(x) for x in trainInputs[0] if x!=0 ],[math.log(x) for x in trainInputs[1] if x!=0]]
    validationInputsNorm = [[math.log(x) for x in validationInputs[0] if x!=0],[math.log(x) for x in validationInputs[1] if x!=0]]
    return trainInputsNorm,validationInputsNorm
   
