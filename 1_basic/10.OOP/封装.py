class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.__battery = 100

    def call(self):
        if self.__battery < 10:
            print("电量不足,请充电")
        else:
            print("正在打电话")
            self.__reduce_battery()

    def __reduce_battery(self):
        self.__battery -= 10


apple = Phone("苹果", 10000)
for i in range(11):
    apple.call()

# print(apple.__battery)  # 报错,不能直接访问私有属性
# apple.__reduce_battery()  # 报错,不能直接访问私有方法
