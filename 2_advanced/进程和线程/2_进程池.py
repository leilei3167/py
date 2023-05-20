# 如果要启动大量子进程,可以使用进程池的方式批量创建子进程


from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    # 创建池,并指定最大进程数,默认是cpu的核数
    p = Pool(6)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all subprocesses done...")
    p.close()  # 调用close()之后就不能继续添加新的Process了,必须关闭
    p.join()  # 对pool对象调用join()方法会等待所有子进程执行完毕
    print("All subprocesses done.")
