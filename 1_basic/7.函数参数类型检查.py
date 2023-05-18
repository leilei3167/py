def my_abs(x):
    # 使用isinstance()函数对参数类型做检查,不符合要求的直接抛出异常
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs(-1), my_abs(-100), my_abs("hel"))


print(isinstance(True, (int, float)))
