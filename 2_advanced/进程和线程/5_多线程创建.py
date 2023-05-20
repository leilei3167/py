import time, threading


# 定义线程要执行的代码


def loop():
    # 获取当前线程的名字
    print("Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("Thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("Thread %s ended." % threading.current_thread().name)


if __name__ == "__main__":
    # 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
    # Python的threading模块有个current_thread()函数，它永远返回当前线程的实例

    print("Thread %s is running..." % threading.current_thread().name)

    t = threading.Thread(target=loop, name="LoopThread")
    t.start()
    t.join()
    print("Thread %s ended." % threading.current_thread().name)


# 线程和进程最大的不同在于，进程中的变量是各自拥有一份，而线程中的变量是共享的,因此多线程就涉及到了线程安全问题
