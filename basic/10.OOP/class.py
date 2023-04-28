# 创建Dog类,类名应该使用驼峰命名
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串,文档字符串用三引号括起,描述类的功能
class Dog():
    """
    一条狗,具备名字和年龄属性,并且能够执行坐下和打滚的行为
    """

    # 类中的函数称为方法
    # __init__()是一个特殊的方法,每当你根据Dog类创建新实例时,Python都会自动运行它
    def __init__(self, name, age):  # self是一个指向实例本身的引用,每当我们根据Dog类创建实例时，都只需给最
        # 后两个形参（name和age）提供值
        """
        Initialize name and age attributes.
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command.
        """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command.
        """
        print(self.name.title() + " rolled over!")


# 根据类创建实例,在出现Dog()时,python会使用实参调用Dog的__init__方法,无需传入self参数,Python会自动传入
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")  # str()函数将非字符串值表示为字符串
print()
my_dog1 = Dog('lucy', 3)
print("My dog's name is " + my_dog1.name.title() + ".")
print("My dog is " + str(my_dog1.age) + " years old.")

print("\nCar类:")


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """
        打印一条指出汽车里程的消息
        """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # setter 可实现对属性的修改,与一些限制性条件
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_car = Car('audi', 'a4', 2016)
print(my_car.get_name())

print("\n修改属性的值:")
my_car.read_odometer()
# 1.直接通过实例修改
my_car.odometer_reading = 23
my_car.read_odometer()

# 2.通过方法修改(setter),能够避免直接修改属性值,从而隐藏实现细节,并且可以添加一些限制条件
my_car.update_odometer(1000)
my_car.read_odometer()
my_car.update_odometer(1)
my_car.read_odometer()
