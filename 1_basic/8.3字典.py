alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")

# 注意，键—值对的排列顺序与添加顺序不同。Python不关心键—值对的添加顺序，
# 而只关心键和值之间的关联关系
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

for i in range(10):
    alien_0["x_position"] += 1
    alien_0["y_position"] += 1

print(alien_0)

print("\n删除键值对")
# 修改字典中的值
alien_0["color"] = "red"
print("修改color为red: ", alien_0)

print("\n删除键值对")
# 删除键值对 使用del
del alien_0["color"]
print("删除color: ", alien_0)

print("\n遍历字典")
# 遍历字典的键值对,需要使用items函数,注意结果是无序的
for k, v in alien_0.items():
    print(k, v)

# 只遍历字典的键
print("\n只遍历字典的键")
for k in alien_0.keys():
    print(k)
# 直接遍历字典时默认只遍历键
for k in alien_0:
    print(k)

print("\n只遍历字典的值")
# 实现有序遍历
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):  # sorted()函数可以对列表进行临时排序
    print(name.title() + ", thank you for taking the poll.")

print("\n遍历字典的值")
for v in favorite_languages.values():
    print(v)

print("\n使用set找出列表中独一无二的元素(去重)")
for v in set(favorite_languages.values()):
    print(v)

# 使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先
# 定义一个空字典
print()
new_map = {}
new_map["name"] = "张三"
print(new_map)

my_list = list(alien_0)  # 只会保留key
print(my_list)

d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d.get("Michael1"))  # 使用get获取不存在的key会返回None
print(d["Michae1l"])  # 直接获取不存在的key会报错 KeyError: 'Michae1l'
