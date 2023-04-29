# 1.继承
import time
from abc import abstractmethod, ABC


# 父类
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self):
        print(f"{self.brand}:{self.price} 正在打电话")


# 子类继承
class Apple(Phone):
    def __init__(self, brand, price, region):
        super().__init__(brand, price)  # 调用父类的__init__方法,初始化父类的属性
        self.region = region  # 子类拓展出的属性

    def call(self):  # 子类重写父类的方法,增加额外的逻辑
        print("call from region:", self.region)
        super().call()  # 调用父类的方法

    def use_face_time(self):  # 拓展出的方法
        print(f"{self.brand}在{self.region}使用FaceTime")


a = Apple("apple", 5000, "中国")
a.call()
a.use_face_time()


# 2.封装,在私有属性前加上双下划线,即可将属性设置为私有属性,只能在类内部访问,外部无法访问
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.__engine = engine

    def run(self):
        self.__start_engine()
        print(f"{self.brand} is running...")

    # 内部方法,只能在类内部调用,外部调用直接报错
    def __start_engine(self):
        print(f"{self.brand} is starting engine {self.__engine}...")
        time.sleep(1)
        print("engine started!")


tesla = Car("tesla", "v8")
tesla.run()


# 3.多态

# 定义抽象类(带有@abstractmethod的类,且继承自ABC就是抽象类),这个抽象类不能实例化,只能被继承(实现),继承他的子类必须实现所有带@abstractmethod的方法
# 相当于go中的接口
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# a = Animal()  # 报错,不能实例化,因为Animal已经是抽象类了


# 具体实现
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"dog: {self.name} age: {self.age} is wang wang wang")

    def move(self):
        print(f"dog: {self.name} age: {self.age} has ran away!!")


# 一个函数,接收一个Animal类型的参数(即接收一个接口类型的实现作为参数),实现多态
def animal_sound(animal: Animal):
    animal.make_sound()
    animal.move()


# 实例,实现接口的多个实例,实现多态
d = Dog("bob", 3)
animal_sound(d)

d2 = Dog("lucy", 2)
animal_sound(d2)


# 没有实现所有的抽象方法,会提示
class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"cat: {self.name} age: {self.age} is miao miao miao")

    def move(self):
        print(f"cat: {self.name} age: {self.age} has ran away!!")


c = Cat("tom", 1)  # 子类并没有实现父类的make_sound方法,但是由于多态,可以正常调用?
animal_sound(c)
