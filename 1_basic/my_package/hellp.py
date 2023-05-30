"""
一个模块开头一定是模块的文档注释


"""

# __all__用来定义from xxx import *时要对外导出的符号(即暴露的接口),但是注意,他只对import * 起作用,对from xxx import xxx不起作用
# 常被init文件调用
# 定义模块级别暴露接口
# all代表了此模块可被外界使用的部分内容
# 没有指定__all__时，from xx import *语句会导入除了以单下划线开头的名称之外的所有对象，可能会导致命名冲突和不可预测的结果
__all__ = ["hello", "Hello"]
__version__ = "0.1"
__author__ = "lei"


def hello():
    print("这是hellp.func()函数")


class Hello:
    def __init__(self, name):
        self.name = name
