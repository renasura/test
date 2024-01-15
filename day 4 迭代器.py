# arr = [1,2,3,4]
# for i in arr:
#     print(i)
# a = iter(arr)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# # str 能不能用迭代器
# b = "hello"
# b = iter(b)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# 自己建立迭代器
class PowTwo:
    """实现迭代器的类
             二的幂"""

    def __init__(self, max = 0):
        self.max = max
    # 定义一个迭代器的参数
    def __iter__(self):
        self.n = 0
        return self
    # 迭代的内容
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration