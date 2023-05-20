# 可以使用Queue,Pipes等多种方式来实现进程间通信


from multiprocessing import Process, Queue
import os, time, random


# 写的子进程,参数是一个Queue
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        v = q.get(True)
        print("Get %s from queue." % v)


if __name__ == "__main__":
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
