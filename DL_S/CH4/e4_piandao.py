import numpy as np
import matplotlib.pylab as plt
#wrong
def func_1(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

x = np.arange(0, 10, 0.1)
y = func_1(x)

plt.plot(x, y)
plt.show()
