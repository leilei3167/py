import os
import shutil

print("操作系统信息")
print(os.uname())  # 系统信息

print(os.environ)  # 所有环境变量

print("获取PATH环境变量: ", os.environ.get("PATH"))  # 指定环境变量

print()
print("操作文件系统,目录的部分一部分在os.path模块中")

print("当前目录的绝对路径: ", os.path.abspath("."))  # 当前目录的绝对路径

print("拼接目录应该使用join而不是直接拼接字符串,因为不同操作系统的路径分隔符不同")
a = "/home/leilei"
b = "py/test.py"
print(os.path.join(a, b))  # 拼接目录

print(
    "拆分目录得到的是一个元组: ",
    os.path.split("/home/leilei/workspace/py/2_advanced/13_os包目录操作.py"),
)
# 注意,返回的是元组,最后一个元素是文件名,前面的是目录
print(
    "获取文件的拓展名: ", os.path.splitext("/home/leilei/workspace/py/2_advanced/13_os包目录操作.py")
)
print(
    "拓展名是第二个元素: ",
    os.path.splitext("/home/leilei/workspace/py/2_advanced/13_os包目录操作.py")[1],
)

print("使用shutil模块复制文件:")
cur = os.path.abspath(".")
src = "test.txt"
dst = "test-dst.txt"


try:
    shutil.copyfile(os.path.join(cur, src), os.path.join(cur, dst))
except Exception as e:
    print("复制文件失败: ", e)
else:
    print("复制文件成功")


print("遍历当前目录筛选某些文件: ")
all_py_files = [
    x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"
]
print(all_py_files)
