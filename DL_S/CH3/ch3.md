### 激活函数
#### 1. step func
+ 阶跃函数是指一旦输入超过阈值,就切换输出的函数。
#### 2. 比较 sigmoid和step func
+ 感知机中神经元之间流动的是 0 或 1 的二元信号,而神经网络中流动的是连续的实数值信号。
+ 当输入信号为重要信息时,阶跃函数和 sigmoid 函数都会输出较大的值;当输入信号为不重要的信息时,两者都输出较小的值。
+ 不管输入信号有多小,或者有多大,输出信号的值都在 0 到 1 之间。
+ 两者均为非线性函数。
#### 3.激活函数必须使用非线性函数
+ 使用线性函数的话,加深神经网络的层数就没有意义
#### 4.ReLU (Rectified Linear Unit)函数(最近主要使用)
+ 在输入大于 0 时,直接输出该值; 在输入小于等于0时,输出0 
#### 5.输出层的激活函数
##### 5.1 机器学习的问题大致可以分为分类问题和回归问题。 
+ 分类问题是数据属于哪一个类别的问题。
+ 回归问题是根据某个输入预测一个(连续的)数值的问题。
##### 5.2 特征
+ 输出为0-1之间的实数，总和为1
+ 即便使用softmax函数,输出值最大的神经元的位置也不会变。因此,神经网络在进行分类时,输出层的 softmax 函数可以省略。
##### 5.3 神经元数量
+ 对于分类问题,输出层的神经元数量一般设定为类别的数量。
##### 5.4 手写识别
1. 用神经网络解决问题时,也需要首先使用训练数据(学习数据)进行权重参数的学习;
进行推理时,使用刚才学习到的参数,对输入数据进行分类。
2. MNIST 数据集是由 0 到 9 的数字图像构成的. 训练图像有 6 万张,测试图像有 1 万张,这些图像可以用于学习和推理。
MNIST 数据集的一般使用方法是,先用训练图像进行学习,再用学习到的模型度量能在多大程度上对测试图像进行正确的分类。
3. 数据为28×28像素灰度图像。各像素取值0-255
