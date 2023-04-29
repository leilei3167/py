# 当使用from xxx import * 时,只会导入__all__列表中的函数

__all__ = ['make_pizza']


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def func():
    print("这是pizza.func2()函数")


# 如果我在模块内本身有测试运行的代码,如果不想这部分代码在其他文件中运行,
# 可以将其放在如下的if语句中
# __name__是一个特殊的变量,用于储存模块的名字,如果运行这个模块,
# 那么他的名字就会是__main__,之后内部逻辑就能够执行
# 如果这个模块被导入到其他文件中,那么这个模块的名字就不是__main__,内部逻辑就不会执行
if __name__ == '__main__':
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
