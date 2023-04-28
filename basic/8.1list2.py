# list的常用操作
# 增删改查

mix_arr = [1, 2.11, "hello", "world", True]
# 1.查元素,返回下标
print("hello所在的索引: ", mix_arr.index("hello"))
# print(mix_arr.index("hello1111"))  # 找不到会报错

# 2.修改元素
mix_arr[0] = 100
print("修改索引0的元素后: ", mix_arr)

# 3.插入 指定索引位置插入元素
mix_arr.insert(1, "插入的元素")  # 在索引1的位置插入元素
print("在索引1插入元素后: ", mix_arr)
mix_arr.insert(10000, "插入10000索引的元素")  # 在索引1的位置插入元素
print("在大于最大容量位置插入元素会直接加在最后: ", mix_arr)

# 4.追加元素
mix_arr.append("追加在最后的元素")
print("append追加元素后: ", mix_arr)

# 5.追加新的列表
arr = [1, 2, 3, 5, 3, 3]
mix_arr.extend(arr)
print("extend追加新的列表后: ", mix_arr)
print("最后一个元素: ", mix_arr[-1])

# 6.删除元素 del 或 pop 或 remove
# del 仅仅删除
del mix_arr[0]
print("del删除索引0的元素后: ", mix_arr)
# pop 不仅能删除,还能将删除的元素返回
mix_arr.pop(1)
print("pop删除索引1的元素后: ", mix_arr)
# remove 指定元素,删除第一个出现的
mix_arr.remove("hello")  # 删除第一个出现的3
print("remove删除第一个出现的hello后: ", mix_arr)

# 8.列表的长度
print("列表的长度: ", len(mix_arr))

# count统计元素出现的次数
mix_arr.count(3)
print("3出现的次数: ", mix_arr.count(3))

# 7.清空列表
mix_arr.clear()
print("clear清空列表后: ", mix_arr)
print("列表的长度: ", len(mix_arr))

# 8.最大值最小值,总和
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("最大值: ", max(digits))
print("最小值: ", min(digits))
print("总和: ", sum(digits))

# 9.切片操作,使用[:]来复制列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("players: ", players)
print("[0:3]:", players[0:3])
print("[-3:]:", players[-3:])  # 最后3个

players1 = ['charles', 'martina', 'michael', 'florence', 'eli']
print("players1: ", players1)
p2 = players1[3:]
print("修改p1之前的p2: ", p2)
players1[3] = "修改后的元素"
print("修改p1之后的p2: ", p2)  # p2不会随着p1的修改而修改
# 复制整个列表
p3 = players1[:]
print("复制整个列表p3: ", p3)
