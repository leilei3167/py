# raise主动抛出异常,异常类型必须是Exception的子类
# raise 异常类型("异常描述")


def test(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("必须是int类型参数")  # 抛出错误
    return a + b


print(test(1, 2))

# 对于可能引发多种错误的操作，可在try代码块中处理多种异常
try:
    print(test(1, "3"))
except ValueError as e:
    print("类型错误: ", e)

print(test(1000, 2))


# 定义自定义异常类,基于Exception类派生,并且重写__str__方法


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):  # 被打印时的错误信息格式
        return f" 我是自定义异常: {self.msg}"


def test2(a, b):
    if type(a) != int or type(b) != int:
        raise MyError("必须是int类型参数")  # 抛出错误
    return a + b


try:
    print(test2(1, "3"))
except ValueError as e:
    print("类型错误: ", e)
except MyError as e:
    print("自定义异常: ", e)

test2(100087, 1010)
