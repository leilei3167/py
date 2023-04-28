import json

numbers = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    2: 1,
    "e": [1, 3, 4, "hello"]
}

filename = "numbers.json"
# 写入json
with open(filename, "w") as file_obj:
    json.dump(numbers, file_obj)  # 将numbers序列化到文件中

# 读取json

with open(filename) as file_obj:
    n1 = json.load(file_obj)
    print(n1)
