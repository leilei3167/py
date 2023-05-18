l = [1, 2, 3, 4, 56, 6]

# 取前三个元素
l03 = l[:3]

print(l03)

# 取后三个元素 记住倒数第一个元素的索引是-1
print("后三个元素: ", l[-3:])
# 修改派生出来的新列表,不会影响原列表,这一点和go语言不同
l03[0] = 100
print("修改派生出的列表后的原列表: ", l)


# 用于原样复制一个列表
l04 = l[:]
print("l04: ", l04)

# 第三个参数是步长,默认为1,可以为负数,表示从右往左取

tmp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tmp[::2])  # 从左往右,每隔两个取一个


# 去除字符串首尾空格
def trim(s):
    # 循环直到首部不是空格
    while s[:1] == " ":
        s = s[1:]

    while s[-1:] == " ":
        s = s[:-1]
    return s


if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")


s = "abcdefg"
print(s[::-1])  # 从右往左取,步长为1,如果步长为负数,则从右往左取,可以实现字符串反转
