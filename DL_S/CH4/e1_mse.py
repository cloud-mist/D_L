import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # 设正确解是 2

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] # 2的概率最高，正确
print(mean_squared_error(np.array(y), np.array(t)))
# 0.09750000000000003

y = [0.1, 0.05, 0.1, 0.0, 0.05,0.1, 0.0, 0.6, 0.0, 0.0] # 7的概率最高，错误
print(mean_squared_error(np.array(y), np.array(t)))
# 0.5975


'''发现例子1的损失函数值更小，即和监督数据误差小, 即更吻合'''


