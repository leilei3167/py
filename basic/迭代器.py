# filter 将一个列表中的元素按照一定的规则进行过滤，返回一个filter对象
fruits = ["apple", "orange", "banana", "pear", "strawberry"]

result = filter(lambda x: "e" in x, fruits)  # 只会保留包含e的元素
print(type(result))  # <class 'filter'>
print(list(result))  # ['apple', 'orange', 'pear', 'strawberry']

# map 将一个列表中的元素按照一定的规则进行运算，返回一个map对象
result = map(lambda x: x + "s", fruits)  # 将每个元素后面加上s
print(type(result))  # <class 'map'>
print(list(result))  # ['apples', 'oranges', 'bananas', 'pears', 'strawberrys']
print(fruits)  # 不会改变原列表
# reduce 用于对参数序列中元素进行累积
from functools import reduce

# x,y分别代表序列中的前两个元素
result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 1+2+3+4+5
print(type(result))  # <class 'int'>
print(result)  # 15
