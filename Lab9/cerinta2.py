from utils import loadData, splitData, myNormalisation, transform
from sklearn.metrics import accuracy_score
from MyLogisticRegression import MyLogisticRegression


if __name__=="__main__":
    #step 1. load data
    inputs,outputs = loadData("iris.data")
    #step 2. split data
    trainInputs, trainOutputs, validationInputs, validationOutputs = splitData(inputs,outputs)
    #step 3. normalisation
    normalisedTrainData, normalisedTestData = myNormalisation(trainInputs,validationInputs)
    #step 4. training
        #train setosa
    classifier = MyLogisticRegression()
    setosaOutputs = [1 if trainOutputs[i]=="Iris-setosa" else 0 for i in range(len(trainOutputs))]
    classifier.fit(normalisedTrainData, setosaOutputs)
    setosaPredict = classifier.predict(normalisedTestData)
       
        #train versicolor
    versicolorOutputs = [1 if trainOutputs[i]=="Iris-versicolor" else 0 for i in range(len(trainOutputs))]
    classifier.fit(normalisedTrainData, versicolorOutputs)
    versicolorPredict = classifier.predict(normalisedTestData)
    
        #train virginica
    virginicaOutputs = [1 if trainOutputs[i]=="Iris-virginica" else 0 for i in range(len(trainOutputs))]
    classifier.fit(normalisedTrainData, virginicaOutputs)
    virginicaPredict = classifier.predict(normalisedTestData)
     
    

    # #step 5. make predictions
    outputs = [[setosaPredict[i],versicolorPredict[i],virginicaPredict[i]] for i in range(len(setosaPredict))]
    labels = [0,1,2]
    computedTestOutputs = []
    for i in range(len(outputs)):
        computedTestOutputs.append(labels[outputs[i].index(max(outputs[i]))])

    # #step 6. evalaute the classifier performance
    error = 0.0
    print("Computed outputs",computedTestOutputs)
    print("Real outputs",transform(validationOutputs))
    for t1, t2 in zip(computedTestOutputs, transform(validationOutputs)):
        error += (t1 - t2) ** 2
    error = error / len(validationOutputs)
    print('prediction error (manual): ', error)




    
