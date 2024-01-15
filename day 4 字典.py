# json 健值对
# a = {"name" : "asura","age" : "18","height" : "170","weight" : "50"}
# print(a.values())得到所有的值
# print(a.get())
# print(a.keys())得到所有的健
# print(a.items())得到分类
# for i in a:
#     print(a.get(i))
# a = input("")
# b = len(a) - 1
# s = ""
# while b >= 0:
#     s = s + a[b]
#     b = b - 1
# print(s)


# from random import randint
#
# a = (randint(1, 100))
# c = 10
# while a < 100:
#     if c == 0:
#         print("游戏结束")
#         break
#     b = int(input("请输入一个整数："))
#     if a > b:
#         print("猜小了")
#
#     if a < b:
#         print("猜大了")
#
#     if a == b:
#         print("猜对了")
#         break
# from random import randint
# a = (randint(1, 3))
# score_玩家 = 100
# score_电脑 = 100
# print("score_玩家 = 100")
# print("score_电脑 = 100")
# print("1为剪刀，2为石头，3为布")
# while True:
#     from random import randint
#
#     a = (randint(1, 3))
#     b = int(input("请输入一个整数："))
#     if b > 3:
#         print("超出范围，1为剪刀，2为石头，3为布")
#     if b == a:
#         print("平局")
#     if a == 1 and b == 2:
#         score_玩家 = score_玩家 - 10
#         print(score_玩家)
#     if a == 1 and b == 3:
#         score_玩家 = score_玩家 + 10
#         print(score_玩家)
#     if a == 2 and b == 1:
#         score_玩家 = score_玩家 + 10
#         print(score_玩家)
#     if a == 2 and b == 3:
#         score_玩家 = score_玩家 - 10
#         print(score_玩家)
#     if a == 3 and b == 1:
#         score_玩家 = score_玩家 - 10
#         print(score_玩家)
#     if a == 3 and b == 2:
#         score_玩家 = score_玩家 + 10
#         print(score_玩家)
#     if score_玩家 == 0 or score_玩家 == 200:
#         break