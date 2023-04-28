print("----------字符串定义的三种方式------------")
# 三种定义字符串的方式
# 1.单引号
s1 = 'hello'
print(s1)
# 2.双引号
s2 = "hello"
print(s2)
# 3.三引号
s3 = '''hello
>>> you -----
are "dsa" \''' 0-0----
fuck ---
'''
print(s3)

print("dsaij\"\"\"\"")

print("----------字符串拼接------------")
# 直接用+号
s4 = s1 + " " + s2 + " you fuck"
print("拼接后:", s4)
n1 = 100
n2 = 300
n3 = 1.222
# s5=s1+" "+n1+" "+n2+" "+n3
# print(s5) # 不能直接和其他类型用加号拼接,需要用str()转换

s5 = s1 + " " + str(n1) + " " + str(n2) + " " + str(n3)
print("s5: ", s5)  # 不能直接和其他类型用加号拼接,需要用str()转换

# 用格式化打印的形式
# 方式一:使用占位符
s5 = "拼接 s1:%s n1:%d n2:%d n3:%f" % (s1, n1, n2, n3)
print(s5)
# 控制打印的精度,如%5d: 输入11,就会变成 [][][]11,会用3个空格补足总共5位宽度
# %.2f小数点精度,会对小数进行四舍五入
s6 = "n3:%.2f" % n3
print(s6)
s7 = "宽度限制2输入121,不会生效:%1d" % 121
print(s7)

# 方式二:快速写法,不限类型,不做精度控制,在字符串内容开始前加f,并使用花括号取变量
print(f"s1:{s1} s2:{s2} n1:{n1} n3:{n3}")

# 直接把表达式写入字符串
print("直接把表达式写入1+1: %d" % (1 + 1))

# title() 使字符串首字母大小写
ti = "python  "
print(ti.title())

# 删除尾部多余空白 必须赋值给原变量才会改变
ti = ti.rstrip()
print(ti)

# 删除首尾空白使用strip()
