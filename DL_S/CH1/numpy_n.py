# 1.5.4 n维数组
import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[3, 0], [0, 6]])

print(A)
print(A.shape)

print(A + B)

print(A * B)    # 也是相对应的点进行乘法 和矩阵法不同
'''[[ 3  0]
    [ 0  24]]'''

print(A * 10)
# 标量 10 被扩展成了 2 × 2 的形状,然后再与矩阵 A 进行乘法运算。这个巧妙的功能称为广播 (broadcast)。
