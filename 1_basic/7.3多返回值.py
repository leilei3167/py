def f1(x, y):
    return "done", x + y, x - y


# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

x = f1(1, 2)
print("多返回值返回的实际上是一个元组: ", x, type(x))

# 可以使用多个变量接收返回值
x, y, z = f1(100, 103)
print(x, type(x), y, type(y), z, type(z))
