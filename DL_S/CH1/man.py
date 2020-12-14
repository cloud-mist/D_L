class man:
    def __init__(self, name):
        self.name = name
        print("init")
    
    def hello(self):
        print("hello "+self.name+"!")

    def bye(self):
        print("bye "+self.name+"!")

m = man("cloud")
m.hello()
m.bye()
# 类Man生成了实例(对象) m 
# 类Man的构造函数(初始化方法)会接收参数 name ,然后用这个参数初始化实例变量 self.name
# 实例变量是存储在各个实例中的变量。
# Python 中可以像 self.name 这样,通过在 self 后面添加属性名来生成或访问实例变量。
