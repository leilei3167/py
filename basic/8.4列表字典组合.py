# 列表中包含字段
d1 = {'name': 'tom', 'age': 20}
d2 = {'abc': 123}
d3 = {'abc': 456}

l = [d1, d2, d3]
print("l中包含字典", l)

print("\n字典中包含列表")
d = {'name': 'tom',
     'age': 20,
     'friends': ['jerry', 'sparrow']
     }
print(d)
