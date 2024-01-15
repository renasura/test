# 面向对象今天
# 三要素 封装 继承 多态 pop
# 父类
class People:  # 创建了一个人的对象
    height = "175cm"  # 属性 身高
    weight = "50kg"
    age = "18"
    face = "cool"
    ID = "10086"
    # 在类里写函数，第一个参数是self
    def say(self):
        print("hello,i my father")
# 子类
class xiaoming(People):
    name = "xiaoming"
    def say(self):
        print("hello,i my son")
# 构造函数编发
print(People.ID)
