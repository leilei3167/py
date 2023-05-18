# 判断一个对象是否是可迭代对象

from collections.abc import Iterable, Iterator

print("字符串是否可迭代: ", isinstance("abc", Iterable))  # str是否可迭代

print("整数是否可迭代: ", isinstance(123, Iterable))
print("列表是否可迭代: ", isinstance([1, 2, 3], Iterable))

# 生成器generator都是可迭代对象,可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator
# 注意,list,dict,str虽然是Iterable,但不是Iterator,他们需要可以通过iter()函数获得一个Iterator对象
print("字符串是否是迭代器: ", isinstance("abc", Iterator))
print("字符串调用iter()后是否是迭代器: ", isinstance(iter("abc"), Iterator))
print("列表是否是迭代器: ", isinstance([1, 2, 3], Iterator))
print("列表调用iter()后是否是迭代器: ", isinstance(iter([1, 2, 3]), Iterator))


# 因为Iterator是一个数据流,所以不能提前知道序列的长度,只能不断通过next()函数实现按需计算下一个数据,
# 所以Iterator的计算是惰性的,只有在需要返回下一个数据时它才会计算

print()
l = [1, 2, 3, 4, 4]
# 转化为Iterator后使用next()函数
it = iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # 抛出StopIteration异常

# 实际上for循环就是通过不断调用next()函数实现的

# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break


# 定义自己的Iterable对象,__iter__和__next__一起定义了一个迭代器


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    # 关键是实现__iter__方法,返回一个迭代器对象(此处是自己)
    def __iter__(self):
        return self

    # for in本质上是调用迭代器的__next__方法,这里定义如何迭代这个类
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index] ** 2
        self.index += 1
        return value


# 这个自定义的类可以用于for in循环,因为它实现了__iter__和__next__方法,自定义的功能是将列表中的每个元素平方
s = MyIterable([1, 2, 3, 4, 5])
for v in s:
    print(v)
