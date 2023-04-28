print("--------------sort永久排序(改变原列表)--------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("before sort: ", cars)
cars.sort()
print("after sort: ", cars)
cars.sort(reverse=True)
print("after sort reverse: ", cars)

print("--------------sorted临时排序(不会改变原列表)--------------")
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print("before sorted: ", cars1)
print("after sorted: ", sorted(cars1))
print("原列表: ", cars1)

print("--------------reverse反转列表(改变原列表)--------------")
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print("before reverse: ", cars2)
cars2.reverse()
print("after reverse: ", cars2)
