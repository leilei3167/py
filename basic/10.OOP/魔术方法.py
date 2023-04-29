# class中的__init__是python的内置的类方法之一,用于初始化一个类的实例
# 这些内置的类方法,各自有其特殊的功能,这些方法被称之为魔术方法(数量比较多)

class Animal:
    # __init__方法:用于构造方法,在创建对象时调用,可以用来对对象进行初始化
    def __init__(self, name, age):
        self._myage = age
        self._myname = name

    # __str__:类似于go中的实现Stringer接口,用于返回一个对象的描述信息(自定义格式化打印这个类),方便我们查看
    def __str__(self):
        return "name:" + self._myname + " age:" + str(self._myage)

    # __lt__:用于比较两个对象的大小,返回bool值
    def __lt__(self, other):
        return self._myage < other._myage

    # 小于大于
    def __le__(self, other):
        return self._myage <= other._myage

    # 类似的还有__gt__,__ge__,__eq__,__ne__


d = Animal("dog", 3)
# 重写__str__方法后,打印对象时,会调用__str__方法,并打印返回值
print(str(d))  # <__main__.Animal object at 0x0000020F4F6F4E80>,默认打印是打印的内存地址

d1 = Animal("dog1", 4)
print(d < d1)  # True
print(d > d1)
d2 = Animal("dog2", 4)
print(d1 <= d2)  # True
