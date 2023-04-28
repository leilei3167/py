import unittest

from name_function import get_formatted_name


# 创建一个继承自unittest.TestCase的类
class NamesTestCase(unittest.TestCase):
    # 以下就是测试用例
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # 断言方法
        self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()
