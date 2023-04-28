# 继承封装多态

# 封装:在私有属性和方法前以下划线开头
class Animal():
    def __init__(self):
        self._myname = "animal"


# 继承
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self._myname = "dog"

    def speak(self):  # 子类新增方法
        print(self._myname, "汪汪汪")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self._myname = "dog"

    def speak(self):  # 子类新增方法
        print(self._myname, "mmm")


# 多态,只接受具有speak方法的对象
def animal_speak(a):
    a.speak()


dog = Dog()
cat = Cat()
animal_speak(dog)
animal_speak(cat)

animal_speak("hello")  # 报错,因为字符串没有speak方法
