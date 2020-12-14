import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
C = np.array([[1,2],[3,4], [4,6]])

print(C.shape)      # (3, 2)   第一个代表行数， 第二个列数
print(np.ndim(A))   # 维数 2

print(np.dot(A, B)) # 矩阵乘法

D = np.array([7,8])
print(D.shape)                  # (2, )  不是两个数的是数组
print(np.array([[7,8]]).shape)  # (1, 2) 矩阵

print(np.dot(C,D).shape)        # (3, )
print(np.dot(C, D))             # [23 53 76]
