# os包能够实现与操作系统的交互，比如获取当前目录，创建目录，删除目录等等,常常用于脚本
import os


# path模块
print(os.path.abspath(__file__))  # 获取当前文件的绝对路径,__file__是一个特殊变量,表示当前文件的相对路径

# getcwd() 获取当前工作目录
current_path = os.getcwd()
print(current_path)

# 创建
# os.mkdir(current_path + "/test") # 不会递归创建目录
os.makedirs(current_path + "/test/test1")  # 会递归创建目录,如果不指定绝对路径,则在当前目录下创建

print("\n 列出当前目录下的所有文件和目录")
data = os.listdir(current_path)
print(data)


# 删除目录,只有空目录才能删除
os.removedirs(current_path + "/test/test1")  # 会递归删除目录,如果不指定绝对路径,则在当前目录下删除
