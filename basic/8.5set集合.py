# 集合使用花括号定义
my_set = {}
my_set1 = {1, 2, 3, 3, 3, 4}  # 内容是无序的,且不重复,重复的会被自动过滤掉
my_set2 = {100, 1000, 200, 3}
print(my_set1)
# 不支持下标索引
# print(my_set1[0])


# 添加元素
print("\n添加元素")
my_set2.add("python")
my_set2.add("python")  # 不会重复添加
print("添加两个python后:", my_set2)

# 删除元素
print("\n删除元素")
my_set2.remove("python")
print("删除一个python后:", my_set2)

# 随机取出元素
print("\n随机取出元素")
print(my_set1.pop())

# 集合清空 clear()

# 两个集合的差集,会得出集合1有,集合2没有的元素
s3 = my_set1.difference(my_set2)
print("set1有set2没有的内容: ", s3)

s4 = my_set2.difference(my_set1)
print("set2有set1没有的内容: ", s4)

# 消除差集(交集),消除集合1中有,集合2中也有的元素
my_set1.difference_update(my_set2)
print("set1消除差集: ", my_set1)

# 集合合并 union()
print("\n集合合并 union()")
my_set3 = my_set1.union(my_set2)
print("合并后的集合: ", my_set3)

print("\n遍历:")
# 集合不能用while循环遍历,只能用for in 循环
for e in my_set3:
    print(e)
