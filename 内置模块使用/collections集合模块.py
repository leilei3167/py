# 相当于使用命名元组,用于表达坐标等等

from collections import namedtuple

print("命名元组: ")
# 创建一个命名元组,表示坐标轴的圆,坐标和半径
Circle = namedtuple("Circle", ["x", "y", "r"])

c = Circle(1, 2, 3)
print(type(c), isinstance(c, tuple), isinstance(c, Circle), c.x, c.y, c.r)


print("\n\n双向列表,可快速向头部增添数据,适合用于队列和栈: ")
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft("left")
print(q)


print("\n\n默认字典,当字典中的key不存在时,返回默认值: ")
from collections import defaultdict

dd = defaultdict(lambda: "N/A")
dd["key1"] = "abc"
dd["key2"] = "def"
print(dd["key1"], dd["key2"], dd["key3"])


print("\n\n有序字典,按照插入的顺序排序: ")
from collections import OrderedDict

d = dict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])
print("默认字典这种顺序并不是 Python 字典的保证行为", d)

d2 = OrderedDict()
for i in range(100):
    d2[str(i)] = i
print("有序字典按照插入key的顺序排列: ", d2)


print("\n\nChainMap,计数器,统计字符出现的次数: ")
from collections import ChainMap
import argparse

# 构造缺省参数:
defaults = {"color": "red", "user": "guest"}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args()
# vars()函数返回对象object的属性和属性值的字典对象
cmd_args = {k: v for k, v in vars(namespace).items() if v}

# 将两个dict合并成一个ChainMap:
combined = ChainMap(cmd_args, defaults)
# 查找时就会按照参数的顺序进行查找,先在命令行参数中查找,如果没有就在默认参数中查找
# 打印参数:
print("color=%s" % combined["color"])
print("user=%s" % combined["user"])


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("name:", self.name, "age:", self.age)


c = Student("zhangsan", 18)
# 字典形式
t = vars(c)
print(type(t), t)
for k, v in t.items():
    print(k, v)
