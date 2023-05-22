# 如果想要向with open一样使用自己的类，需要实现__enter__和__exit__方法
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print("Begin")
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print("Error")
#         else:
#             print("End: ", traceback)
#
#     def query(self):
#         print("Query info about %s..." % self.name)
#
#
# with Query("Bob") as q:
#     q.query()
import threading

# contextlib提供了更简单的方法


from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s..." % self.name)


@contextmanager
def create_query(name):
    print("Begin")
    q = Query(name)
    # 使用yield将函数分割为两部分,前半部分在__enter__中执行,后半部分在__exit__中执行
    # yield返回值会赋值给as后面的变量
    yield q
    print("End")


# with语句首先执行yield之前的语句,因此打印出Begin
# yield之后调用with内部的所有语句(即缩进部分),因此打印出Query info about bob...
# 最后执行yield之后的语句,因此打印出End
with create_query("bob") as c:
    c.query()


# closing可以把任意对象自动关闭,这个对象就是一个上下文管理器，它的__exit__函数仅仅调用传入参数的close函数

from urllib.request import urlopen

from contextlib import closing

with closing(urlopen("https://www.python.org")) as page:
    print(type(page))  # http.client.HTTPResponse
    for line in page:
        print(line)


# with语句:
# with 上下文管理器 [as 变量]:
#       code-block1
#       code-block2
# as 变量是可选的,如果指定了,其就是调用上下文管理器的__enter__方法的返回值
# 执行顺序:
# 1.调用函数创建上下文管理器对象
# 2.调用上下文管理器对象的__enter__方法,如果指定了as 变量,则将__enter__方法的返回值赋值给变量
# 3.执行with语句中的代码块即code-block1和code-block2
# 4.执行上下文管理器对象的__exit__方法,并将异常信息传递给__exit__方法


# 如open("1.txt") as f:返回的f就是上下文管理器对象,其就是个文件对象
# 如果我们要自定义一个上下文管理器，只需要定义一个类并且是实现__enter__()和__exit__()即可


@contextmanager
def locked(lock):
    lock.acquire()
    try:
        yield
    finally:
        lock.release()


l = threading.Lock()

with locked(l):
    # 自动上锁
    print("do something")
    # 执行完毕自动释放锁
