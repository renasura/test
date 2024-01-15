class Animal:
    # type_ = ""
    # eat = ""
    # voice = ""
    def __init__(self,type_,eat,voice):
        self.type_ = type_
        self.eat = eat
        self.voice = voice
# 构造函数的作用是可以从外界创建属性
dog_ = Animal(type_ = "dog",eat = "gouliang",voice = "wang")
print(dog_.type_)
