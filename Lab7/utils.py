import csv
import os
import matplotlib.pyplot as plt 

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

def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

def showPlots(inputs,outputs):
    plotDataHistogram(inputs[0], 'capita GDP')
    plotDataHistogram(inputs[1], 'freedom')
    plotDataHistogram(outputs, 'Happiness score')

    ax = plt.axes(projection='3d')
    ax.scatter3D(inputs[0], inputs[1], outputs, c=outputs, cmap='Greens')
    plt.title('GDP capita & freedom vs. happiness')
    plt.xlabel('GDP capita')
    plt.ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.show()