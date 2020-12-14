import numpy as np
import matplotlib.pylab as plt

def relu_func(x):
    return np.maximum(x, 0)

x = np.arange(-5.0, 5.0, 0.1)
y = relu_func(x)

plt.plot(x, y)
plt.show()
