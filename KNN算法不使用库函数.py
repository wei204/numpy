import csv
import math
import operator
import random
import matplotlib.pyplot as plt
import seaborn as sns
# 下载数据集  读取  并且分为训练集与测试集
def loadDataset(filename,split,trainingSet = [],testSet = []):
    with open(filename,'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        print(dataset)
    for x in range(len(dataset)):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])
    print(dataset)

# 计算euclideanDistance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# 计算出测试实例与所有训练集点的距离  并设定k个临近点
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# 将距离测试实例最近的几个训练集的点进行分类
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedvotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    print(classVotes)
    print('sortedVotes:',sortedvotes)
    return sortedvotes[0][0]


# 精确度
def getAccuracy(testSet,predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'E:\pyitem\numpy\iris.data.txt', split, trainingSet, testSet)
    print('Trainset:', repr(len(trainingSet)))
    print('Testset:', repr(len(testSet)))
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet,testSet[x],k)
        result = getResponse(neighbors)
        predictions.append(result)
    accuracy = getAccuracy(testSet,predictions)
    print('Accuracy:',repr(accuracy)+'%')
    plt.plot(predictions[:, 0], predictions[:, 1], '.')
    plt.show()
main()