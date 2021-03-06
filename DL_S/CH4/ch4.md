## 神经网络学习
### 1.定义
+ “学习”是指从训练数据中自动获取最优权重参数的过程
+ 为了使神经网络能进行学习,将导入损失函数这一指标. 学习的目的就是找出能使函数值达到最小的 `权重参数`
+ 那么使用什么方法？ 函数斜率的梯度法 
### 2.实现识别5的方案
#### 2.1 特征量方案
+ Define:先从图像中提取特征量, 再用机器学习技术学习这些特征量的模式。
+ 特征量:是指可以从输入数据(输入图像)中准确地提取本质数据(重要的数据)的转换器。
+ 特征量是向量形式，用这些转换成向量（常用的特征量包括SIFT、SURF 和 HOG 等),
再使用机器学习中的 SVM、KNN 等分类器进行学习.
+ 针对不同方案，特征量需要认为考虑。
#### 2.2 神经网络方案
+ 直接进行端到端的学习，无需人工干预
### 3.一些机器学习概念
+ 为什么区别训练数据和测试数据？ 追求的是模型的泛化能力
+ 泛化能力： 处理未被观察过的数据(不包含在训练数据中的数据)的能力
+ 过拟合 (over fitting): 只对某个数据集过度拟合的状态.处理其他数据集就拉跨。
+ one-hot :将正确解标签表示为 1,其他标签表示为 0 的表示方法称为 
### 4 损失函数
#### 4.1 定义
+ 神经网络的学习通过某个指标表示现在的状态。以这个指标为基准,寻找最优权重参数.
神经网络的学习中所用的指标称为损失函数 (loss function)
+ 可以使用任意函数,但一般用`均方误差和交叉熵误差`等。
+ 表示神经网络性能的“恶劣程度”的指标,即当前的神经网络对监督数据在多大程度上不拟合,在多大程度上不一致。
#### 4.2 交叉熵误差
+ 交叉熵误差的值是由正确解标签所对应的输出结果决定的。
#### 4.3 mini-batch
+ 使用训练数据进行学习,严格来说,就是针对训练数据计算损失函数的值,找出使该值尽可能小的参数。
+ 如果训练数据有 100 个的话,我们就要把这 100 个损失函数的总和作为学习的指标。最后要进行正规化，即除以个数。
+ 拿出一部分数据来估计总体。例如：如果训练数据有 100 个的话,我们就要把这 100 个损失函数的总和作为学习的指标。
#### 4.4 为什么要有损失函数
+ 为了找到使损失函数的值尽可能小的地方,需要计算参数的导数(确切地讲是梯度),然后以这个导数为指引,逐步更新参数的值。
+ 在进行神经网络的学习时,不能将识别精度作为指标。  
因为如果以识别精度为指标,则参数的导数在绝大多数地方都会变为 0。
+ sigmoid 函数的导数在任何地方都不为 0,神经网络的学习得以正确进行。
+ 阶跃函数的导数在绝大多数地方(除了 0 以外的地方)均为0.  
也就是说,如果使用了阶跃函数,那么即便将损失函数作为指标,参数的微小变化也会被阶跃函数抹杀,导致损失函数的值不会产生任何变化。
### 5.数值微分
#### 5.1 偏导数
+ 保持一个变量为常数即不变， 再用正常的求导公式带入求导。
+ 即：偏导数需要将多个变量中的某一个变量定为目标变量,并将其他变量固定为某个值。
### 6.梯度
#### 6.1 概念
+ **梯度**：由全部变量的偏导数汇总而成的向量称为梯度 (gradient)。

+ 梯度指向函数 f(x 0 ,x 1 ) 的“最低处”(最小值)一样,所有的箭头都指向同一点; 其次,我们发现离“最低处”越远,箭头越大;
更严格地讲,梯度指示的方向是各点处的函数值减小最多的方向

+ **梯度法**：通过巧妙地使用梯度来寻找函数最小值(或者尽可能小的值)的方法就是梯度法.  
函数取值从当前位置沿着梯度方向前进一定距离,再在新地方重新求梯度,再沿新梯度方向前进,如此反复,不断地前进。

+ 函数的极小值、最小值以及被称为鞍点 (saddle point)的地方,梯度为 0;   
*鞍点* 是从某个方向上看是极大值,从另一个方向上看则是极小值的点;   
当函数很复杂且呈扁平状时,学习可能会进入一个(几乎)平坦的地区,被称为“学习高原”的无法前进的停滞期.

+ **学习率**： 式(4.7)的 η 表示更新量,在神经网络的学习中,称为学习率 (learningrate)。  
学习率*决定* 在一次学习中,应该学习多少,以及在多大程度上更新参数;  
学习率*需要* 事先确定为某个值;一般会一边改变学习率的值,一边确认学习是否正确进行,取的过大或过小都不行;  
实验结果表明:学习率过大的话,会发散成一个很大的值;反过来,学习率过小的话,基本上没怎么更新就结束了。也就是说,设定合适的学习率是一个很重要的问题。
#### 6.2 神经网络的梯度
+ **定义**:损失函数关于权重参数的梯度
