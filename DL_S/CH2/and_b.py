# 用权重和偏置实现

import numpy as np

def AND(x1, x2):

    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1