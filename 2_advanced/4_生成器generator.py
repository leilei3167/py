# 列表表达式可以快速生成列表，但是如果列表元素过多，会占用大量内存,如果列表的元素可以通过某种算法推算出来，
# 那么我们是否可以在循环的过程中不断推算出后续的元素呢？ 这样就避免了一开始就创建一个完整的list，从而节省大量的空间。

from collections.abc import Iterable

print("第一种方法,将列表生成式的[]改成()就创建了一个generator")

g = (x if x % 2 == 0 else -x for x in range(1, 10))  # 如果是偶数,则保留,否则取反
print(type(g), g, " 是否可迭代: ", isinstance(g, Iterable))  # <class 'generator'>

# 通过next()函数获得generator的下一个返回值,generator保存的是算法,每次调用next(g)就计算出g的下一个元素的值,
# 直到计算到最后一个元素,没有更多的元素时,抛出StopIteration的错误

# generator也是Iterable对象,因此可以使用for循环
for i in g:
    print(i)


print("\n第二种方法,将函数中的return改成yield,就创建了一个generator")


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"


f = fib(10)
print(type(f))
for i in f:
    print(i)


# 最难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5
    return "this is a return value"  # 如果要获取return的值,需要捕获StopIteration错误,返回值包含在StopIteration的value中


o = odd()
print(next(o))  # 调用next时会执行,直到遇到yield
print(next(o))  # 再次调用next时会从上次yield处继续执行,直到遇到下一个yield
print(next(o))

# 一般情况下拿不到return的值,如果想要获取return的值,需要捕获StopIteration错误,返回值包含在StopIteration的value中
while True:
    try:
        print(next(o))
    except StopIteration as e:
        print(e.value)  # 获取return的值
        break


# 生成器: 杨辉三角
def triangles(size):
    if size < 1:
        return None
    L = [1]
    yield L
    for i in range(2, size + 1):
        L = [1] + [L[j - 1] + L[j] for j in range(1, i - 1)] + [1]  # 两侧永远都是1
        yield L


t = triangles(5)
for i in t:
    print(i)


print()
print()
l1 = [1, 2, 3]
l2 = [2, 4, 5]
l3 = l1 + l2
print("len: ", len(l3))
print(l3)

print()
l1.append(l2)
print("len: ", len(l1))
print(l1)
