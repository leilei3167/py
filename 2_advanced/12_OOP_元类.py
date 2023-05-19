# 函数和类的定义，不是编译时定义的，而是运行时动态创建的

# type函数除了可以返回一个对象的类型外，还可以用来创建出新的类型
# 如果要通过type创建一个class对象，需要提供三个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

Hello = type(
    "Hello", (object,), dict(hello=lambda self: print("Hello,world!"))
)  # 调用type在运行的时候动态创建新的class
h = Hello()
h.hello()

# 使用metaclass创建类
# 类就像实例的模板,创建实例前要先创建类,但是如果想创建出类,就必须根据metaclass创建出类
# metaclass->class->instance 可以把类看成是metaclass创建出来的“实例”
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码,但是好在基本不会用到


# metaclass是类的模板,所以必须从type类型派生
# 元类名称始终以Metaclass结尾,以便清楚地表示这是一个元类
class ListMetaclass(type):
    # 准备创建的类的名称,类继承的父类集合,类的方法集合
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)  # 给类增加方法
        return type.__new__(cls, name, bases, attrs)


# 有了元类后,皆可以根据这个元类创建出类,然后创建出实例
# 通过指定metaclass=ListMetaclass,就会调用ListMetaclass.__new__()来创建类
class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add(1)
l.add(11)
l.add(111)
print(l)

# 运行时创建和修改类的寻求常见于ORM中 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来
