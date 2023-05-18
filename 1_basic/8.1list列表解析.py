# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素

squares = [
    value**2 for value in range(1, 11)
]  # for循环为for value in range(1,11)，它将值1~10提供给表达式value**2,此处循环不加冒号
print(squares)
