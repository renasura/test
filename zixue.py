# %s 将内容变成字符串
# %d 将内容变成整数
# %f 将内容变成浮点数
# %m.n 宽度为m 小数点精读为n
# f"{占位}"
# if嵌套
# for i in range(1000, 10000):
#     a = i // 1000
#     b = i // 100 % 10
#     c = i // 10 % 100 % 10
#     d = i % 10
#     if a ** 4 + b ** 4 + c ** 4 + d ** 4 == i:
#         print(i)
# year = int(input("请输入年份:"))
# month = int(input("请输入月份:"))
# day = int(input("请输入日期:"))
# count_day = 0
# nian = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year % 4 == 0 or year % 400 == 0:
#     print("今年是闰年")
#     nian[1] = 29
# else:
#     print("今年是平年")
#     nian[1] = 28
#
# for i in
count =  0
for a in range(1,21):
    for b in range(1,34):
        c = 100- a -b
        if c > 0 and a * 5 + b * 3 +c * 1 / 3 == 100:
            count = count + 1
            print(f"第{count}种算法，公鸡的数量为{a},母鸡的数量为{b},小鸡的数量为{c}")

