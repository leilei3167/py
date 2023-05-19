class Student(object):
    # 装饰器,可以将这个getter方法当成属性来使用
    @property
    def score(self):
        return self._score

    # 如果只定义property不设置setter,则该属性为只读属性
    @score.setter
    def score(self, value):
        # 可以在此增加各种判断逻辑
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value


s = Student()
s.score = 60  # 实际上转化为s.set_score(60)
print(s.score)  # 实际上转化为s.get_score()


class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # 只读属性
    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print("resolution =", s.resolution)
if s.resolution == 786432:
    print("测试通过!")
else:
    print("测试失败!")
