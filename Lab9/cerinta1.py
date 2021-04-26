from utils import loadData, splitData, normalisation, transform, myNormalisation
from sklearn import linear_model
from sklearn.metrics import accuracy_score


if __name__=="__main__":
    #step 1. load data
    inputs,outputs = loadData("iris.data")
    #step 2. split data
    trainInputs, trainOutputs, validationInputs, validationOutputs = splitData(inputs,outputs)
    #step 3. normalisation
    normalisedTrainData, normalisedTestData = normalisation(trainInputs,validationInputs)
    #step 4. training
    classifier = linear_model.LogisticRegression()
    classifier.fit(normalisedTrainData, transform(trainOutputs))
   
    #step 5. make predictions
    computedTestOutputs = classifier.predict(normalisedTestData)

    #step 6. evalaute the classifier performance
    print("Computed outputs", computedTestOutputs)
    print("Real outputs", transform(validationOutputs))
    error = 1 - accuracy_score(transform(validationOutputs), computedTestOutputs)
    print("classification error (tool): ", error)

    
