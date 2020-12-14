import numpy as np
import matplotlib.pylab as plt

def sigmoid_func(x):
    return 1/(1 + np.exp(-x))
# x可以为numpy数组，因为广播的功能。

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid_func(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
