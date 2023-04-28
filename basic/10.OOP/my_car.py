# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
# 而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
# 一次导入多个类
from car import ElectricCar, Car

# 创建普通car
my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())

# 创建电动car,可以直接使用父类的方法
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
# 使用属性中的类的实例
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
