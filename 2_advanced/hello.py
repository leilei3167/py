__author__ = "lei"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


# 模块内私有变量和函数以单下划线开头


def __some_private():
    print("This is a private function!")


class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        self.__nick_name()

    def __nick_name(self):
        print("nick name", self.name.lower())


if __name__ == "__main__":
    test()
