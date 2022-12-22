import numpy as np
import operator
import kNN


def creatDataSet():
    group = np.array([[1, 1.1], [1, 1], [0, 0], [0.1, 0]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet   # np.tile将输入的向量形式转换成与训练样本中向量形式相一致
    sqdiffMat = diffMat ** 2
    # print(sqdiffMat)
    sqDistances = sqdiffMat.sum(axis=1)
    # print(sqDistances)
    distances = sqDistances ** 0.5     # 由17-22 计算欧式距离
    sortedDistIndicies = distances.argsort()  # 按照从小到大的顺序排列，输出其对应的索引值
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = kNN.creatDataSet()
    kind = kNN.classify0([0.5, 0.5], group, labels, 3)
    print(kind)