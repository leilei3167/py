import time
import unittest

from mydict import Dict


# TestCase类内置了很多断言方法
class TestDict(unittest.TestCase):
    # setup和teardown,分别在单元测试前后运行,可以在这里做一些初始化的工作和后续的清理工作
    # 会在每一个测试方法运行前后分别被执行,注意是每一个测试方法,而不是每一个测试类
    def setUp(self):
        print("setup...")
        print("假装连接mysql...")
        print("假装连接redis...")
        time.sleep(2)
        print("初始化完成!")

    def tearDown(self):
        print("teardown...")
        print("清理测试产生的临时文件...")
        time.sleep(2)
        print("关闭完成!")

    # 测试方法要以test_开头 不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def test_init(self):
        d = Dict(a=1, b="test")
        # 断言是否相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        # 断言是否为True
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)  # 断言key属性是否在d中
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        # 断言抛出指定类型的Error
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行单元测试
if __name__ == "__main__":
    unittest.main()
