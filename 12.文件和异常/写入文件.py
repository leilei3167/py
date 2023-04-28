with open("2.txt", "w") as file:
    for i in range(10):
        file.write(f"hello python[{i}]\n")

# w是写入,会覆盖原有内容,如果文件不存在,会创建文件
# a是追加,不会覆盖原有内容,如果文件不存在,会创建文件
# r+ 是读写,不会覆盖原有内容,如果文件不存在,会报错
# 省略时默认是以只读模式打开文件

with open("2.txt", "a") as file:
    for i in range(100, 120):
        file.write(f"hello c[{i}]\n")
