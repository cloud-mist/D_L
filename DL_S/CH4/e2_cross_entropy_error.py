import numpy as np

def cross_entropy_error(y, t):

    delta = 1e-7
    return -np.sum(t*np.log(y+delta))
''' 1.当正确解标签对应输出越大，式子越接近0；如果较小，值较大
    2.加delta,是保护。防止log0的负无限大的情况发生'''

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

result = cross_entropy_error(np.array(y), np.array(t))
print(result)   # 0.510825457099338

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result = cross_entropy_error(np.array(y), np.array(t))
print(result) # 2.302584092994546

# log是e为底的
