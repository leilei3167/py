# 使用装饰器

from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec


def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)
    for para_name, para_type in hints.items():
        if para_name == "return":
            continue
        if not isinstance(kwargs[para_name], para_type):  # 检查参数值是否符合类型
            raise TypeError(f"Parameter {para_name} must be {para_type}")


def type_check(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):  # 定义一个装饰器函数
        # 类似于反射,获取被装饰函数的所有参数
        func_args = getfullargspec(decorator)[0]  # 取出函数定义的参数名
        kwargs.update(dict(zip(func_args, args)))  # 将参数和值组成字典
        validate_input(decorator, **kwargs)  # 对参数进行类型检查
        return decorator(**kwargs)  # 验证通过,执行被装饰函数

    return wrapped_decorator


if __name__ == "__main__":

    @type_check
    def add(a: int, b: int) -> int:
        return a + b

    # 相当于
    # add = type_check(add)

    print(add(1, 2))

    print(add(1, "2"))
