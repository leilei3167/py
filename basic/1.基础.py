# 数据类型 有三种:string,整数,浮点数

# 使用type()检查变量存储的类型
s = "hello world"
d = 19
f = 3.1415926

print(type(s))
print(type(d))
print(type(f))

# python是弱类型语言，变量的类型可以随时改变
f = "dsajio"
f_type = type(f)
print("f的type的type", type(f_type))

print("-----------------数据转换----------------------")
# 数据类型之间的转换
# int() 将其他类型转换为整数
# float() 将其他类型转换为浮点数
# str() 将其他类型转换为字符串
# bool() 将其他类型转换为布尔值

print("int float 丢失精度 (3.14)=", int(3.14))
print("int str 字符串转数字 必须只有数字 (3)=", int("3"))
print("float int (3)=", float(3))
# print("float str (hellp)=",float("hello")) # 会报错
print("bool 0=", bool(0))
print("bool 100=", bool(100))  # 除了0都是true
print("bool -100=", bool(-100))

print("-----------------标识符----------------------")
_name = "pig"
print(_name)
_Name = "pig1"
print(_Name)

# class="ndias"
# print(class)
print("class是关键字，不能作为变量名")
print("python的变量名区分大小写,一般命名为小写字母，多个单词用下划线隔开")
my_name_is = "pig2"
print(my_name_is)
