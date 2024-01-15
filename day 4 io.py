# IO 输入输出 对文件的操作
# 打开文件
# 读取写入操作
# 关闭文件
# f = open("/Users/asura/Desktop/test.png","r",encoding="utf-8")
# for i in f:
#     print(i)
# print(f.read(4))
# f.close()
# 获取当前目录下的文件用列表表示
import os
# 目录路径
print(os.getcwd())
print(os.listdir())
# 利用代码建立文件夹
for i in range(1,2):
    os.mkdir("/Users/asura/Desktop/wenjianjia{}".format(i))