import sys, os
sys.path.append(r"/home/cloudmist/study/D_L/CH3")
import numpy as np

from CH3.func_softmax_v3 import softmax
from e5_gradient import numerical_gradient

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
