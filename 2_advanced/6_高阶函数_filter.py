# filter会根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1  # 只保留奇数


# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 相当于是一个生成器表达式: (item for item in iterable if is_odd(item))


# 生成器,生成从3开始的奇数序列,这种写法是无限的序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 返回一个闭包,这个闭包的作用是用于filter,判断传入的数否能被n整除,如果不能整除,则返回True,否则返回False
def _not_divisible(n):
    return lambda x: x % n > 0


# 生成器,不断返回下一个素数,这种写法是无限的序列,可以用于表示所有的素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        # 注意it被更新为一个新的生成器,而不是立刻算出所有的结果,获取结果是在n=next(it)时才会计算
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 30:
        print(n)
    else:
        break


# 筛选回文数,正向遍历和反向遍历的结果相同的数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


# output = filter(is_palindrome, range(1, 1000))
# print("1~1000:", list(output))
# if list(filter(is_palindrome, range(1, 200))) == [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     11,
#     22,
#     33,
#     44,
#     55,
#     66,
#     77,
#     88,
#     99,
#     101,
#     111,
#     121,
#     131,
#     141,
#     151,
#     161,
#     171,
#     181,
#     191,
# ]:
#     print("测试成功!")
# else:
#     print("测试失败!")

# 简化版本
print(list(filter(lambda x: str(x) == str(x)[::-1], range(1, 10000))))
