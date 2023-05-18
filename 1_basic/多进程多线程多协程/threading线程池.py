import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import time

# 创建线程锁
lock = threading.Lock()


# 线程锁可以创建全局变量让每个线程都能访问,而进程锁不行,进程锁必须使用Manager().Lock()创建并作为参数传递给子进程
def work(i):
    lock.acquire()
    print(i)
    time.sleep(1)
    lock.release()
    return f"{i} done {os.getpid()}"


if __name__ == "__main__":
    results = []
    t = ThreadPoolExecutor(5)
    for i in range(20):
        r = t.submit(work, (i,))  # 提交任务到线程池并执行
        results.append(r)

    for res in results:
        print("返回值: ", res.result())

    # 线程池无需考虑join的问题,因为线程池内部已经实现了join
    print("线程池内所有任务已经执行完毕")
