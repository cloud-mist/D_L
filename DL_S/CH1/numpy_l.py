import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(type(x))
    
print(x-y)          # 对应元素运算 ，必须有相同元素个数
print(x*y)

print(x/2.0)        # 标量运算（广播）


'''     Result
<class 'numpy.ndarray'>
[-1. -2. -3.]
[ 2.  8. 18.]
[0.5 1.  1.5]
'''

