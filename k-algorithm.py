import kNN
import numpy as np
import operator


group, labels = kNN.creatDataSet()
# print(group, labels)
# print(group.shape)  # 四行两列
# print(np.tile([1, 2], [2,2]))
# a = np.array([[1, 2]])
# print(a.sum(axis=1))


# 分类器  inX为待分类向量，dataSet为训练样本集，labels为标签，k为选择最近邻居的数目
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
    kNN.classify0([0.5, 0], group, labels, 3)