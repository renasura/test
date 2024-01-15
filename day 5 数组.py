# 在python数组叫列表
# 区别，数组只能将同一种类型的数据放在一起，列表可以把多种类型的数据放一起
# import array
# c = array.array
# sum_ = 0
# b = 2.0
# a = 1.0
# for i in range(1,21):
#     sum_ += a / b
#     t = a
#     a = a + b
#     b = t
# print(sum_)
sum_ = 0

for i in range(1, 21):
    c = 1
    for j in range(1, i + 1):
        c = c * j
    sum_ += c

print(sum_)
# 1! + 2! + 3!
