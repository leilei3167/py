import time
import os
import multiprocessing

# # 串行执行
# def workA():
#     for i in range(10):
#         print(i, "a ", os.getpid())
#         time.sleep(0.5)
#
#
# def workB():
#     for i in range(10):
#         print(i, "b ", os.getpid())
#         time.sleep(0.5)
#
#
# if __name__ == "__main__":
#     t1 = time.time()
#     workA()  # 串行执行,可以看到进程号都是一致的
#     workB()
#     print(time.time() - t1)


# 将a在一个子进程中执行,实现并行执行
def workA():
    for i in range(10):
        print(i, "a ", os.getpid())
        time.sleep(1)


def workB():
    for i in range(10):
        print(i, "b ", os.getpid())
        time.sleep(1)


if __name__ == "__main__":
    t1 = time.time()
    a_p = multiprocessing.Process(target=workA)
    b_p = multiprocessing.Process(target=workB)

    # 一次启动多个进程
    process = []
    for p in (a_p, b_p):
        process.append(p)
        p.start()

    # 等待所有子进程执行完毕再继续执行主进程
    for p in process:
        p.join()

    # 判断进程是否存活
    for p in process:
        print(p, p.is_alive())  # 两个进程都已经执行完毕,所以都是False

    print("耗时: ", time.time() - t1)
