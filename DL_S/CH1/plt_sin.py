import matplotlib.pyplot as plt
import numpy as np

# 1.生成数据
x = np.arange(0, 10, 0.1)           # 以0.1为单位，生成0-10 的数据
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label="sin") # 图例
plt.plot(x, y2, linestyle = "--", label="cos") # 用虚线

plt.xlabel("x") # x轴的标签
plt.ylabel("y")

plt.title("sin and cos") # 整个图的标题
plt.legend() # 传入图例的值进行显示

plt.show()
