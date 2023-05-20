# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
# 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁

import threading

# 全局的Local对象,每个线程只能读写和自己相关联的副本,互不干扰,能够自动处理锁的问题,最常用的地方就是为每个线程绑定一个数据库连接,HTTP请求等
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=("Alice",), name="Thread-A")
t2 = threading.Thread(target=process_thread, args=("Bob",), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()
