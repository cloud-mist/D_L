# 求导
'''1.利用三点中心差分，减小误差
    2.使用过小值，无法正确表示，因此用1e-4'''

import numpy as np
import matplotlib.pylab as plt

def numberical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
# 传递 函数f和f的参数

def func_1(x):
   return 0.01 * x **2 + 0.1 * x

x = np.arange(0.0, 20.0, 0.1)
y = func_1(x)

def func_2(x):
    k = numberical_diff(func_1, 5)
    b = 0.75 - 5.0*k
    y = k*x + b
    return y
y2 = func_2(x)

print(numberical_diff(func_1, 5))
print(numberical_diff(func_1, 10))
#0.1999999999990898     0.2999999999986347

# 给x, y加标签
plt.xlabel("x")
plt.ylabel("f(x)")

plt.plot(x, y, label = "f(x)") # 加图例
plt.plot(x, y2, label = "k=n_d(func_1, 5)",linestyle="--")
plt.legend()
plt.show()



