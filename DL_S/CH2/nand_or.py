import numpy as np
# nand & or 

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w*x)+b

    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.7, 0.7])
    b = -0.5

    tmp = np.sum(w*x)+b

    if tmp <= 0:
        return 0
    else:
        return 1

