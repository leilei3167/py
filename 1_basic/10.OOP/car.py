from battery import Battery


# 父类
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """汽车有油箱"""
        print("Done!")


# 子类,电动车,父类必须包含在当前文件中，且位于子类前面
class ElectricCar(Car):  # 定义子类时，必须在括号内指定父类的名称
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        # super()是一个特殊函数(父类又叫超类)，帮助Python将父类和子类关联起来,相当于调用父类的实例方法
        super().__init__(make, model, year)  # 2.初始化父类的属性
        # 初始化父类之后,可以初始化子类的属性
        self.battery_size = 70
        self.battery = Battery()  # 将实例用作属性

    # 子类的方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 重写父类的同名方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
