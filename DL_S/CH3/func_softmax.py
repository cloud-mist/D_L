# softmax 函数
import numpy as np

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)           # 对数组求指数
print(exp_a)

sum_exp_a = np.sum(exp_a)   # 再求和
print(sum_exp_a)            # 74.1221542101633

y = exp_a / sum_exp_a       # 每个都除以指数和
print(y)                    # [0.01821127 0.24519181 0.73659691]
