# 装饰器其实就是闭包,只不过是通过@语法糖来实现的


def wrapper(func):
    print("func:", func)

    # 注意,args,和kwargs代表的是参数,列表和字典,所以要加*和**才能传参,这样能够接收任意参数
    def inner(*args, **kwargs):
        print("装饰器正在验证权限...")
        print("args:", args)
        print("kwargs:", kwargs)
        r = func(*args, **kwargs)
        print(r)
        print("装饰器执行完毕...")

    return inner


@wrapper  # @wrapper等价于f = wrapper(sleep)
def sleep(name, age):
    import random
    import time

    if age < 10:
        return "未成年人禁止睡觉"

    time.sleep(random.randint(1, 3))
    return f"{name}:{age} 在睡觉中..."


# 直接调用sleep函数,会先执行wrapper函数,然后执行sleep函数
# sleep("bob", 10)
# print()
# sleep(age=19, name="Bob")


# 类的装饰器,有很多种
# 1.classmethod,必须把cls作为第一个参数
class Test:
    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls):
        print("run")

    def jump(self):
        print("jump")

    @staticmethod
    def sleep():
        print("sleep")


# 区别:类方法的第一个参数是类本身,而实例方法的第一个参数是实例本身
# 类方法可以通过类名调用,也可以通过实例调用


t = Test("dsa")
print(t.name)
t.run()  # 通过实例调用类方法,没问题,但如果不想实例时也想调用方法呢?
t.jump()

Test.run()  # 通过类名调用类方法,没问题,但是如果想在类中调用类方法呢?
# Test.jump()  # 类不经初始化只能调用带有装饰器的方法 Test.jump() missing 1 required positional argument: 'self'

# 2.staticmethod,声明为静态方法,不接受参数
# 静态方法可以通过类名调用,也可以通过实例调用
Test.sleep()


# 3.property:把一个方法变成一个静态属性


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 通过property装饰器,把一个方法变成一个静态属性(getter),静态属性设置必须通过setter装饰器
    @property
    def info(self):
        return f"{self.name}:{self.age}"

    # 通过setter装饰器,把一个方法变成一个静态属性
    @info.setter
    def info(self, value):
        self.name, self.age = value.split(":")


t = Person("bob", 18)
print(t.info)  # 通过property装饰器,把一个方法变成一个静态属性,而不是方法调用
t.info = "alice:20"  # 通过setter装饰器,把一个方法变成一个静态属性,而不是方法调用
print(t.info)
