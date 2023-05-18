# 集合可用于取交集并集的操作
set1 = {1, 2, 3, 4, 5}
set2 = {10086, 4, 5, 1000}
set3 = {1, 2, 3, 4, 100, 101, 102}

print(set1 & set2 & set3)  # 交集,即多个集合中都有的元素
print(set1 | set2 | set3)  # 并集,即两个集合中所有的元素,不重复

# 字典的key必须是不可变对象,那么元组是否可以?
k = (
    1,
    2,
)

kmap = {k: "hello"}
print(type(kmap), kmap)

# 如果是元组中有可变对象,则不可以做key,因为无法hash计算hash值
k2 = (1, 2, [4, 6])
kmap2 = {k2: "hello"}
print(type(kmap2), kmap2)
