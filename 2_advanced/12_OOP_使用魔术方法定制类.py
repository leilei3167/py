# class中的__init__是python的内置的类方法之一,用于初始化一个类的实例
# 这些内置的类方法,各自有其特殊的功能,这些方法被称之为魔术方法(数量比较多)


class Animal:
    __myage = 0
    __myname = ""

    # __init__方法:用于构造方法,在创建对象时调用,可以用来对对象进行初始化
    def __init__(self, name: str, age: int):
        self.__myname = name
        self.__myage = age

    # __str__:类似于go中的实现Stringer接口,用于返回一个对象的描述信息(自定义格式化打印这个类),方便我们查看
    # 定制print时的打印信息,使打印的信息更加有意义
    def __str__(self):
        return "name:" + self.__myname + " age:" + str(self.__myage)

    # __getattr__:用于获取属性,当访问的属性不存在时,会调用__getattr__方法,返回自定义的信息或者返回某个属性,而不是直接抛异常
    def __getattr__(self, item):
        return f"访问的item: {item} 不存在"

    # __setattr__:用于设置属性,当设置属性时,会调用__setattr__方法,可以在这里对属性进行一些检查和限制
    # key是当前的属性名字,value是要设置的值
    def __setattr__(self, key, value):
        if key == "_Animal__myage" and value < 0:
            raise ValueError("年龄不能为负数")
        else:
            super().__setattr__(key, value)  # 验证通过,调用父类的__setattr__方法,设置属性

    # 使得实例对象可以像函数一样被调用,即重写__call__方法
    # s=Animal()
    # s()  # 这样会调用__call__方法
    def __call__(self, *args, **kwargs):
        print("__call__方法被调用了!!")

    # __lt__:用于比较两个对象的大小,返回bool值
    def __lt__(self, other):
        return self.__myage < other.__myage

    # 小于大于
    def __le__(self, other):
        return self.__myage <= other.__myage

    # 类似的还有__gt__,__ge__,__eq__,__ne__

    # 私有属性通过getter和setter方法来访问

    @property
    def age(self):
        return self.__myage

    @age.setter
    def age(self, value):
        self.__myage = value


d = Animal("dog", 3)
# 重写__str__方法后,打印对象时,会调用__str__方法,并打印返回值
print(str(d))  # <__main__.Animal object at 0x0000020F4F6F4E80>,默认打印是打印的内存地址

d1 = Animal("dog1", 4)
print(d < d1)  # True
print(d > d1)
d2 = Animal("dog2", 4)
print(d1 <= d2)  # True


print()
print(d.age)
d.age = 5
print(d.age)
print(d.hello)
# d.age = -1
print(d.age)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    # 如果希望类能够像for in一样迭代,需要实现__iter__方法,返回一个迭代器(具有__next__方法的对象)
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # __getitem__:用于获取元素,当访问的元素不存在时,会调用__getitem__方法,返回自定义的信息 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    # 注意,n可能是索引,也可能是切片对象slice
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1

            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for i in Fib():
    print(i)

f = Fib()
print(f[0])
print(f[6])
print(f[12])
