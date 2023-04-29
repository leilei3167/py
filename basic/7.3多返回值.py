def f1(x, y):
    return "done", x + y, x - y


x = f1(1, 2)
print(x, type(x))

# 可以使用多个变量接收返回值
x, y, z = f1(100, 103)
print(x, type(x), y, type(y), z, type(z))
