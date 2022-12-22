import numpy as np
import cv2
import matplotlib.pyplot as plt
# file = open('E:\\pyitem\\numpy\\test1.txt')
#
# lines = file.readline()
# for l in lines:
#     print(l, end='')

# a0 = np.array([[1, 2], [3, 4]])
# a = np.zeros(np.shape(a0))
# a1 = np.tile(a0, (2, 2))
# print(a1)
# print(a0)
# print(a)

# a = plt.figure()
# a = a.add_subplot(111)
# a.scatter([0, 1, 2], [0, 2, 4])
# plt.show()

# # 矩阵对应点相乘
# mat_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# mat_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(mat_1*mat_2)
# # 矩阵相乘
# print(np.dot(mat_1, mat_2))

# # 将某段距离分成若干份
# x = np.linspace(0, 2*np.pi, 100)
# print(x, x.dtype)    # float64
# # 创建单位矩阵
# y = np.eye(3)
# y1 = np.identity(3)
# print(y, y.dtype)
# print(y1)
# 创建随机大小的矩阵
# z = np.random.randint(1, 9, (3, 3), dtype=np.uint8)
# print(z, z.dtype)
# 矩阵的转置
# z_t = z.T
# print(z_t, z_t.shape)
# z_t1 = z.transpose()
# print(z_t1)
# 转换矩阵形状
# x1 = x.reshape(-1, 100)
# print(x1, x1.shape())
# z1 = z.reshape(1, 9)  # z1为2维
# print(z1, z1.shape)
# z11 = z.reshape(-1)
# print(z11, z11.shape) # z11为1维
# z2 = z.flatten()  # z2为1维  与z.ravel()功能相同
# print(z2, z2.shape)

# 按行合并两个矩阵
# y_z = np.hstack([y, z])
# print(y_z, y_z.dtype, y_z.shape)
# # 按列合并两个矩阵
# y_z_v = np.vstack([y, z])
# print(y_z_v)

# # 计算矩阵每列的最大值
# z_l_max = z.max(axis=0)
# print(z_l_max)
# # 计算矩阵每行的最大值
# z_h_max = z.max(axis=1)
# print(z_h_max)

# 矩阵对应元素平方
# z_p = np.power(z, 2)
# print(z_p)
# 矩阵的开方
# z_s = np.power(z, 0.5)
# z_s1 = np.sqrt(z)
# print(z_s, z_s.dtype)
# print(z_s1, z_s1.dtype)
# 矩阵的对数
# z_log = np.log(z)
# print(z_log)
# z_log2 = np.log2(z)
# print(z_log2)
# # 矩阵的乘法
# # 产生一个一维向量
# x = np.array([[1, 2, 3]])
# print(x, x.shape)
# x_t = x.T
# print(x_t, x_t.shape)
# # 按照对应元素相乘
# print(z*x)
# print(z*x_t)
# # 按照矩阵与向量相乘
# # print(z@x_t)

# 矩阵元素的获取
# 取第一行
# z_h = z[0, :]   # 取第0行，每一列都要取
# print(z_h)
# # 取第一列
# z_l = z[:, 0]  # 取每一行，第一列
# print(z_l)
# a = np.ones((5, 5))
# print(a[0:5, 0:4])
# print(a[1:4, 1:4])

# # 对矩阵归一化
# x = np.random.randint(0, 10, (3, 3))
# print(x)
# range = x.max(0) - x.min(0)
# x_dis = x - np.tile(x.min(0), (3, 1))
# print(x.min(0))
# print(np.tile(x.min(0), (3, 1)))
# print(x_dis)
# x_norm = x_dis / np.tile(range, (3, 1))
# print(x_norm, type(x_norm))
# # print(x)
# # print('每列最小值：', x.min(0))
# # print('每行最小值：', x.min(1))