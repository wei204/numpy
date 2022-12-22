import numpy as np
# 创建一维数组
a = np.array([0, 1, 2, 3, 4])
# print(a.shape, type(a))
# 选择数组元素
b = np.array([[1, 2], [3, 4]])
print(b[0])    # [1 2]
print(b[0, 1])   # 2
# numpy数据类型
c0 = 12
c = np.float64(c0)
print(c)
# 复数类型
d = np.complex64(6+4j)
print('实部为:', d.real, '虚部为:', d.imag)
e = np.array([1, 2], dtype=complex)
print(e)   # [1.+0.j 2.+0.j]
e1 = np.array([1+5j, 2])
print(e1)  # [1.+5.j 2.+0.j]
# 处理数组形状
x = np.arange(48).reshape(2, 4, 6)  # 形状为将0~48 分成两个四行六列的数组
print(x)
# 将多维数组转为一维数组
y = np.array([[0, 1, 2], [3, 4, 5]])
print(y.ravel())  # [0 1 2 3 4 5]
y1 = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(y1)
# print(y1.ravel())
print(y1.flatten())
# 转置
z = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(z.transpose())
# 调整大小
z1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
z1.resize((2, 2, 2))
print(z1)
# 堆叠数组
a11 = np.arange(0, 9).reshape(3, 3)
b11 = 2 * a11
print('水平堆叠：', np.hstack((a11, b11)))
a12 = np.arange(0, 16).reshape(4, 4)
b12 = 2 * a12
print('串联堆叠：', np.concatenate((a12, b12), axis=1))
a13 = np.array([[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]])
print('横向拆分：', np.hsplit(a13, 4))
a14 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
a14.resize(1, 9)  # a14发生改变
print('改变形状：', a14)
print('转置：', a14.transpose())