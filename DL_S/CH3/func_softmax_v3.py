# 为了解决溢出问题。对此函数进行合理化改变。
import numpy as np
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)

print(np.sum(y))        # 1.0 因为输出总和为1,所以可以把输出解释为概率
