from utils import loadData, splitData,flatten,normalisation
import matplotlib.image as mpimg
from sklearn import neural_network
from sklearn.metrics import accuracy_score

if __name__=="__main__":
    inputs, outputs = loadData("data.csv")
    trainInputs, trainOutputs, validationInputs, validationOutputs = splitData(inputs,outputs)
    trainInputsFlatten = [flatten(el) for el in trainInputs]
    validationInputsFlatten = [flatten(el) for el in validationInputs]


    trainInputsNormalised, validationInputsNormalised = normalisation(trainInputsFlatten, validationInputsFlatten)

    classifier = neural_network.MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=1000, solver='sgd', verbose=10, random_state=1, learning_rate_init=.1)
    classifier.fit(trainInputsNormalised,trainOutputs)
    predictedLabels = classifier.predict(validationInputsNormalised)

    print("Real labels: ", validationOutputs)
    print("Computed labels: ", predictedLabels)
    acc = accuracy_score(validationOutputs, predictedLabels)
    print("Accuracy: ",acc)





