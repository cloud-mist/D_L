import numpy as np

x = np.array([0, 1])            # input
w = np.array([0.5, 0.5])        # 权重
b = -0.7                        # 偏置  theta = -b

print(w*x)                      #         [0.  0.5]
print(np.sum(w*x) + b)          # result: -0.19999999999999996
