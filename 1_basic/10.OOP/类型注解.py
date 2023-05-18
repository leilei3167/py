# 类型注解可以帮助IDE对数据的类型进行推断和检查
import random
from typing import Union, Dict


def func():
    return "hello"


# 1.在变量后跟冒号进行类型注解(一般在无法直接看出类型时添加,如函数返回值)
name: str
name = "hello"
v1: int = 10
v2: str = "hello"
v3: bool = True
v4: list[int] = [10, 20, 30]  # 类型是列表，列表中的元素都是int类型
v5: tuple[int, str, bool] = (10, "dsa", False)  # 可以单独指定元组中每个元素的类型
v51: tuple[int, ...] = (10, 12, 44)  # 也可以不指定
v6: dict[str, str] = {"name": "孙悟空", "age": "18"}  # key和value的类型都是str
v9: Dict[str, float] = {"name": 123, "age": 18}  # 这种形式也可以
v1 = 2.3  # 由于类型注解的存在，IDE会对这行代码进行警告
v6["name"] = 123  # 由于类型注解的存在，IDE会对这行代码进行警告

# 1.1 在注释中进行类型注解
vv1 = random.randint(1, 10)  # type: int

vv2 = func()  # type: str


# 2.函数和方法的参数注解,def 函数名(形参名1:类型1,形参名2:类型2)->返回值类型:
def add(x: int, y: int) -> int:
    return x + y


# 3.使用Union类型进行联合类型注解,需要导入Union模块
# 如何对混合类型的数据进行注解?
vvv1 = [1, 2, 3, "helo", True]  # 列表中的元素可能是int,str,bool类型
vvv2: list[Union[int, str, bool]] = [1, 2, 3, "helo", True]  # 列表中的元素可能是int,str,bool类型
vvv3: dict[str, Union[int, str]] = {"name": "孙悟空", "age": 18}  # 字典中的value可能是int,str类型


# data参数要么是int要么是str,返回值也是int或str
def func2(data: Union[int, str], y: str) -> Union[int, str]:
    pass
