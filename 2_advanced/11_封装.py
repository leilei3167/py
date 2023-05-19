class Student(object):
    count = 0

    def __init__(self, name, gender):
        self.name = name
        # 双下划线开头的变量是私有变量，只有内部可以访问，外部不能访问,会将其修饰为_Student__gender
        self.__gender = gender
        Student.count += 1  # 访问类属性,可以计算实例化调用的次数,假设实例有和类属性同名的属性,则会覆盖类属性(删除实例属性后,类属性又会生效)

    def get_gender(self):
        return self.__gender

    def set_gender(self, g):
        if g != "male" and g != "female":
            return False
        self.__gender = g
        return True


bart = Student("Bart", "male")
if bart.get_gender() != "male":
    print("测试失败!")
else:
    bart.set_gender("female")
    if bart.get_gender() != "female":
        print("测试失败!")
    else:
        print("测试成功!")
