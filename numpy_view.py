import scipy.misc
import matplotlib.pyplot as plt
# # 获取面部图片
# face = scipy.misc.face()
# # 创建副本
#
# face_copy = face.copy()
# # 创建视图
# face_view = face.view()
# # 改变视图中的值
#
# face_view.flat = 0
# # 显示视图
# plt.subplot(221)
# plt.imshow(face)
# plt.subplot(222)
# plt.imshow(face_copy)
# plt.subplot(223)
# plt.imshow(face_view)
# plt.show()


# 花式索引，将图片对角线数据置为零
face = scipy.misc.face()
print(face.shape)
xmax = face.shape[0]  # x轴最大像素值
ymax = face.shape[1]  # y轴最大像素值
# print(xmax)
face = face[:min(xmax, ymax), :min(xmax, ymax)]
# print(face)
xmax = face.shape[0]  # x轴最大像素值
ymax = face.shape[1]  # y轴最大像素值  此时face变成正方形数组
# print(ymax)
# face.flags.writeable = True
face[range(xmax), range(ymax)] = 0

# print(face)
face[range(xmax-1, -1, -1), range(ymax)] = 0
plt.imshow(face)
plt.show()