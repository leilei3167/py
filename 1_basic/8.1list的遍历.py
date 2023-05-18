mix_arr = [1, 2.11, "hello", "world", True]

# range函数可以生成一个整数序列,而可以通过list转换为列表
print(list(range(5)))  # [0, 1, 2, 3, 4]

# for in 使用长度
length = len(mix_arr)
for index in range(length):
    print(f"下标[{index}]遍历:", mix_arr[index])

# for in 使用直接列表
print()
for item in mix_arr:
    print("遍历:", item)

# while
print()
index = 0
while index < length:
    print(f"下标[{index}]遍历:", mix_arr[index])
    index += 1

# enumerate
print()
for index, item in enumerate(mix_arr):
    print(f"下标[{index}]遍历:", item)


# pop遍历并清空
while mix_arr:
    print("pop:", mix_arr.pop(0))
