# 三层神经网络的实现

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))
# 0 -> 1
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) # 2*3
B1 = np.array([0.1, 0.2, 0.3])

print(X.shape,"\n", W1.shape, "\n", B1.shape)   # (2,) (2, 3) (3,)
A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1)
print(A1)
print(Z1)


# 1->2
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) # 3*2
B2 = np.array([0.1, 0.2])

print(Z1.shape, " ", W2.shape," ", B2.shape)        # (3,)   (3, 2)   (2,)
A2 = np.dot(Z1, W2) + B2

Z2 = sigmoid(A2)


# 2 -> 3
def identity_func(x):   # 输出层的激活函数
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3 

Y = identity_func(A3)
print(Y)
