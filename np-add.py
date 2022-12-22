import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
from matplotlib import pyplot as plt


# # 加载iris数据集,将第一列数据作为x坐标值，第二列数据作为y坐标值，图上的点用‘.’表示
iris = load_iris()
# print(iris.DESCR)
data = iris.data
plt.plot(data[:, 0], data[:, 1], '.')
plt.show()
#
#
# # 加载波士顿数据集
# boston = load_boston()
# data = boston.data
# plt.plot(data[:, 3], data[:, 4], '+')
# plt.show()


# 实现两个向量组相加，一个向量为0~n-1的二次幂，另一个为0~n-1的三次幂
def vector_add(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    # print(a, b)
    for i in range(n):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i]+b[i])
    # return c
    print(c)


def vector_add_numpy(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    print(a, b)
    c = a + b
    print(c)


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
plt.plot(a, b, 'g-', label='aa')   # a,b分别为xy坐标，‘g-’表示绿色实线
plt.show()

# if __name__ == '__main__':
    # vector_add(3)
    # vector_add_numpy(3)