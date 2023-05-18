# 有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任
# 意数量的实参。
# 在形参名前加星号代表这个参数是一个元组,两个星号代表这个参数是一个字典

# 在定义函数时参数上加星号让Python创建一个名为toppings的空元组，并将收到的所有值都封
# 装到这个元组中

print("\n传递任意数量的实参,在定义函数时参数上加星号,多个参数会被封装到元组中")


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("values: ", toppings, "type: ", type(toppings))
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni", "dsacxz", "dueh")

print("\n结合使用位置实参和任意数量实参,不定数量的实参必须放在最后")


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

print("\n使用任意数量的关键字实参,在形参**user_info中，Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中")


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():  # user_info是一个字典
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
