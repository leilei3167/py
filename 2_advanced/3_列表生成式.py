# 用于快速生成列表, (start,end, step) ,分别为起始值,结束值,步长
import os

# 基本用法
l = list(range(1, 10, 2))
print(l)

# 可以直接在列表内循环和使用表达式
l1 = [x * x for x in range(1, 10)]
print(l1)

# 等价于
l = []
for x in range(1, 10):
    l.append(x * x)
print(l)


# 还可以加上if判断

l2 = [x * x for x in range(1, 10) if x % 2 == 0]  # 只有偶数的平方
print(l2)


# 两层循环
l3 = [m + n for m in "ABC" for n in "XYZ"]
print(l3)


# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir(path=".")])


# 将字段key和value互换
d = {"a": 1, "b": 2, "c": 3}
print({v: k for k, v in d.items()})


l4 = ["ABC", "HELP", "XYZ"]
print([s.lower() for s in l4])

print(l4)  # 不会改变原来的列表


# 对于列表生成式中的if,在for之前的是一个表达式,必须产生一个结果因此必须加else,而for之后的if是一个过滤条件只需产生布尔值,不能加else

l5 = [x if x % 2 == 0 else -x for x in range(1, 10)]  # 如果是偶数,则保留,否则取反
print(l5)

l2 = [x * x for x in range(1, 10) if x % 2 == 0]  # 如果x是偶数,则筛选通过
print(l2)


# 仅仅将其中的字符串变为小写
L1 = ["Hello", "World", 18, "Apple", None]
L2 = [x.lower() if isinstance(x, str) else x for x in L1]
print(L2)

# 排除非字符串
L3 = [x for x in L1 if isinstance(x, str)]
print(L3)
