from math import sqrt

def sumListMAE(r1, c1):
    sum = 0.0
    for i in range(len(r1)):
        sum += abs(r1[i] - c1[i])
    return sum

def sumListRMSE(r1, c1):
    sum = 0.0
    for i in range(len(r1)):
        sum += (r1[i] - c1[i]) ** 2
    return sum

def predictionError(realOutputs, computedOutputs):
    # MAE
    errorL1 = sum(sumListMAE(r,c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)

    # RMSE
    errorL2 = sqrt(sum(sumListRMSE(r, c) ** 2 for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs))
    return errorL1, errorL2

def evalClassification(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)
    return acc, precision, recall 

def multiTargetPredictionError():
    realOutputs = [[3, 5, 8], [1, 2, 7], [4, 6, 9], [10, 11, 12]]
    computedOutputs = [[2.8, 5, 7.7], [1, 2.3, 7.1], [4.3, 5.9, 9], [10.1, 11, 11.9]]
    print('Prediction error:')
    error1, error2 = predictionError(realOutputs, computedOutputs)
    print('Error1 (MAE) = '+str(error1))
    print('Error2 (RMSE) = '+str(error2))
    print('')


def multiClassEval():
    realLabels = ["dog", "cat", "cat", "horse", "dog", "horse"]
    labels = ["dog", "cat", "horse"]
    computedLabels = ["dog", "cat", "horse", "cat", "dog", "horse"]
    acc, precision, recall = evalClassification(realLabels, computedLabels, labels)
    print("Accuracy: " + str(acc) + " Precision: " + str(precision) + " Recall: " + str(recall))

if __name__ == "__main__":
    multiTargetPredictionError()
    multiClassEval()
