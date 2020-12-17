# 求梯度
import numpy as np
import matplotlib.pylab as plt

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # 生成和x形状相同,所有元素都是0的数组

    for idx in range(x.size):
        tmp_val = x[idx]

        #计算f(x+h) 和 f(x-h)
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 还原值

    return grad

def func_2(x):
    return np.sum(x**2) # y = x^2 + y^2

# 可以算出每个点的梯度值。
t1 = numerical_gradient(func_2, np.array([3.0, 4.0]))
print(t1)

t2 = numerical_gradient(func_2, np.array([0.0, 2.0]))
print(t2)

t3 = numerical_gradient(func_2, np.array([3.0, 0.0]))
print(t3)

#[ 6.  8.]
#[ 0.  4.]
#[ 6.  0.]

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_his = []  # 记录画图的值
                        # f：要进行优化的参数，lr学习率; 
    for i in range(step_num):
        x_his.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr * grad # 梯度×学习率再更新。step_num 指定重复次数 

    return x, np.array(x_his)


# test
init_x = np.array([-3.0, 4.0])
t4, x_his = gradient_descent(func_2, init_x = init_x, lr=0.1, step_num=20)
print(t4)           # [-6.11110793e-10  8.14814391e-10] 找最小值，结果非常接近(0, 0)

# draw
plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_his[:,0], x_his[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()
