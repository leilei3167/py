# assert用于判断一个表达式，在表达式条件为False的时候触发异常,抛出AssertionError
assert 1 == 1
# assert 1 == 2, "1!=2"  # AssertionError


def test(a, b):
    assert type(a) == int and type(b) == int, "必须是int类型参数"
    return a + b


print(test(1, 2))
# print(test(1, "2"))


def test2(*nums):
    assert len(nums) > 0, "至少传入一个参数"
    # 判断所有元素是否都是int类型
    # all 函数接受一个可迭代对象作为参数，如果可迭代对象中的所有元素都为真值，则返回 True，否则返回 False
    # 此处遍历取出nums中的每个元素,判断是否都是int类型
    assert all([type(i) == int for i in nums]), "参数必须全部是int类型参数"
    return sum(nums)


print(test2(1, 2, 3, 4, 5))
print(test2(1, 2, 3, "4", 5))
