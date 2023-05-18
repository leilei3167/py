# 有时候你需要创建一系列不可修改的元素 元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组
# 元组使用圆括号来标识，而不是方括号
d = (200, 50, 1, 2, 3, 4, 44, 66)
print("d:", d, "type:", type(d))

# 尝试修改
# d[0] = 1 # TypeError: 'tuple' object does not support item assignment


# 遍历元组中的所有值和列表一样
for i in d:
    print(i)

# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都
# 不变，可使用元组

# 如果要定义只有1的元组
d = 1
print(type(d))  # <class 'int'> 这是一个整数而不是一个元组
d = (1,)  # 正确方式
print(type(d))  # <class 'tuple'>

# 元组是不可变的但是其中如果有元素是列表,列表是可变的(或其他引用类型)
d = (1, 2, 3, [1, 2, 3], {"name": "zhangsan"})
d[3][0] = 10086
d[4]["name"] = "lisi"
print(d)

# 空元组
d = ()
print(type(d))
