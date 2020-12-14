# 画阶跃函数

import numpy as np
import matplotlib.pylab as plt

def step_func(x):
    return np.array(x>0, dtype=np.int)  
# x>0会将其中的元素转换为布尔类型，但是需要int型的0/1，用后面那个进行转换 


x = np.arange(-5.0, 5.0, 0.1)
y = step_func(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
plt.show()

# 当>=0 为1,当<0 输出为0.这个特别像上升沿

