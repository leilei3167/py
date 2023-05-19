import hello


hello.test()
hello.__some_private()  # python没有办法强制让包的私有函数不被调用

c = hello.MyClass("Lei")

c.print_name()
# c.__nick_name()  # 类的私有属性和方法可以使用双下划线
