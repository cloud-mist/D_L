import numpy as np
# 访问

x = np.array([[0, 10], [20, 30], [40, 50]])

# 指定索引访问
print(x)                        # 
print(x[0])                     # [ 0 10] 
print(x[0][1],"\n")             # 10

# for 分行访问 
for row in x:
    print(row)

# 变为1维访问
x = x.flatten()                 # 变为一维
print(x)                        # [ 0 10 20 30 40 50]
print(x[np.array([0, 2, 4])])   # [ 0 20 40]

print(x[x>15])                  # [20 30 40 50]



