import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("/home/cloudmist/wallpapers/youyi.png") # 读入图像,不能用～来表示家目录
plt.imshow(img) # 显示图的方法

plt.show()
