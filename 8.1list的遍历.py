mix_arr = [1, 2.11, "hello", "world", True]

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
