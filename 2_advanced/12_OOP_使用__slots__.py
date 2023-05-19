# python中的class定义好之后,实例化的对象可以任意绑定属性和方法,这一点和go是完全不同的,go的struct是不能动态绑定属性和方法的


class Student:
    pass


s = Student()
s.name = "Michael"  # 动态给实例绑定一个属性


def set_age(self, age):  # 定义一个函数作为实例方法,如果要给所有的实例都绑定方法,可以给class绑定方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 动态的给实例绑定一个方法也是可以的,在程序运行过程中给实例添加方法

s.set_age(19)
print(s.name, s.age)


# 如果想要限制实例的属性,比如只允许对Student实例添加name和age属性,就可以利用__slots__变量


class Student2:
    # 限制Student2只能添加name和age属性
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称


s2 = Student2()
s2.name = "dhsau"
s2.age = 12
# s2.score = 99  # AttributeError: 'Student2' object has no attribute 'score'


class Student3:
    # 可防止添加新的属性,实现类似于go的struct
    __slots__ = ("__name", "__age", "__job")

    def __init__(self, name, age, job):
        self.__name = name
        self.__age = age
        self.__job = job

    def introduce(self):
        print(
            "My name is %s, I'm %d years old, I'm a %s"
            % (self.__name, self.__age, self.__job)
        )


s3 = Student3("dhsau", 12, "student")
s3.introduce()
# s3.score = 99  # AttributeError: 'Student3' object has no attribute 'score'
