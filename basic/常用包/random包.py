import random

print(random.random())  # 生成0-1之间的随机数
print(random.random())  # 生成0-1之间的随机数
print(random.random())  # 生成0-1之间的随机数

print()

print(random.randint(1, 10))  # 生成1-10之间的随机数
print(random.randint(10, 100))
print(random.randint(111, 12212))

print()
print(random.uniform(1, 10))  # 生成1-10之间的随机float数
print(random.uniform(1, 10))  # 生成1-10之间的随机float数
print(random.uniform(1, 10))  # 生成1-10之间的随机float数

print("choice返账对象中的一个随机元素")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(a))
print(random.choice(a))
print(random.choice(a))
b = "hello world"
print(random.choice(b))
print(random.choice(b))
print(random.choice(b))
print(random.choice(b))

print("sample")
print(random.sample(a, 3))  # 从a中随机取出3个元素
print(random.sample(a, 5))
print(random.sample(a, 2))

print("randrange")  # 此处的步长为2,只会取偶数
print(random.randrange(0, 100, 2))  # 从0-100之间随机取出一个数,步长为2
print(random.randrange(0, 100, 2))  # 从0-100之间随机取出一个数,步长为2
print(random.randrange(0, 100, 2))  # 从0-100之间随机取出一个数,步长为2
# 等价于
print(random.choice(range(0, 100, 2)))
