# multiprocessing包提供了跨平台的多进程支持，multiprocessing模块提供了一个Process类来代表一个进程对象

import os
import time
from multiprocessing import Process

# 定义子进程要执行的代码和参数


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))
    time.sleep(2)
    print("Child process %s end." % os.getpid())


if __name__ == "__main__":
    # 父进程pid
    print("Parent process %s." % os.getpid())  #
    # 创建子进程类，传入执行函数和参数,参数以元组的形式传入
    p = Process(target=run_proc, args=("test",))
    p.start()  # 启动子进程
    p.join()  # 可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print("Child process end and main process will exit")
