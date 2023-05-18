# sorted通过一个key函数来实现自定义的排序，例如按绝对值大小排序等
l = [36, 5, -12, 9, -21]
print(sorted(l))  # 默认按照从小到大排序


# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted(l, key=abs))  # 按照绝对值从小到大排序


# 对字符串排序，是按照ASCII的大小比较的
print(sorted(["bob", "about", "Zoo", "Credit"]))  # Z在前面，因为ASCII码小


# 忽略大小写排序(将字符串全部转换为小写再排序)
print(sorted(["bob", "about", "Zoo", "Credit"], key=str.lower))


# 反向排序
print(sorted(["bob", "about", "Zoo", "Credit"], key=str.lower, reverse=True))


L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]


def by_name(t):
    return t[0].lower()


print(sorted(L, key=by_name))


def by_score(t):
    return t[1]


print(sorted(L, key=by_score, reverse=True))
