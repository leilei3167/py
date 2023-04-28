# list列表

# 语法 [1,3,3,4,5]
arr = [1, 2, 3, 4, 5]
str_arr = ["hello", "world"]
mix_arr = [1, 2.11, "hello", "world", True]  # 列表中的元素可以是不同类型的,和js一样
nested_arr = [1, [1, 2, 3], 3, 4, ["hel", "abc", [True, False]]]  # 随意嵌套

# 定义空列表两种方式
arr1 = []
arr2 = list()

# 使用下标取出元素
print(arr[0])  # 1
print(arr[1])  # 2
print(mix_arr[1])
print(nested_arr[1][1])  # 2
print(nested_arr[4][2][0])  # False

# 可以反向索引,-1为最后一个元素,-2为倒数第二个元素以此类推
print(arr[-1])  # 5
print(nested_arr[-1][-1][-1])  # False

# 索引越界,会报错
# print(arr[5])  # IndexError: list index out of range
