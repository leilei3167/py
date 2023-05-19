class Animal(object):
    pass


# 大类,哺乳动物继承自动物类,鸟类继承自动物类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 可以飞的动物
class RunnableMixIn(object):
    def run(self):
        print("Running...")


class FlyableMixIn(object):
    def fly(self):
        print("Flying...")


# 具体的动物就可以多重继承了,比如狗继承自哺乳动物和可跑的动物:
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn
class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Eagle(Bird, FlyableMixIn):
    pass


# 多重继承的目的是从两种继承树中分别选择并继承出子类,这种设计通常称之为MixIn
# MixIn类一般会有一组方法或属性,这些方法和属性可以被其他类直接混入使用,从而获得其提供的功能
# Mixin可以理解为是一种组合行为,将多个类的功能组合到到一起实现代码功能模块的复用
# (类似于go的struct的嵌套,将多个struct的功能和属性组合到一起)
