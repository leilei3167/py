# 1.直接读取
# 关键字with在不再需要访问文件后将其关闭,推荐
with open("1.txt") as file_obj:
    contents = file_obj.read()  # read 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行
    # 相比于原文多了一个空行 删掉即可
    print(contents.rstrip())

# obj2 = open("1.txt") # 不推荐
# c = obj2.read()
# print(c)
# obj2.close()  # 不用with的话必须手动关闭文件


print("\n逐行读取:")
# 2.逐行读取
with open("1.txt") as file_obj:
    # 直接遍历文件对象
    for line in file_obj:
        print(line.rstrip())

print("\n逐行放入列表后在外部使用:")
with open("1.txt") as file_obj:
    # 将各个行放入列表中
    lines = file_obj.readlines()

# 外部可以使用这个列表
pi = ""
for i in lines:
    pi += i.strip()

print(pi)
