# 进程过多会造成资源浪费，进程池可以解决这个问题,对于进程池来说，进程池中的进程是可以复用的,减少进程的创建和销毁
import multiprocessing
import os
import time


def work(count, lock):
    lock.acquire()  # 加锁
    print(count, os.getpid())
    time.sleep(3)  # 需要加锁的代码
    lock.release()  # 释放锁
    return f"result: {count} pid: {os.getpid()}"


# 进程锁可以解决进程之间的资源竞争问题
if __name__ == "__main__":
    # 创建池
    pool = multiprocessing.Pool(5)
    # 创建进程锁,manager是一个进程管理器,可用于进程间的交互,lock是他提供的一个锁对象
    manager = multiprocessing.Manager()
    lock = manager.Lock()  # 将锁作为参数传递给进程函数,加锁之后各个进程之间就不能同时执行了

    results = []  # 收集各个进程执行任务的返回值
    for i in range(20):  # 开启20个任务,但是池中只有5个进程,所以每次只能并行执行5个任务
        result = pool.apply_async(work, args=(i, lock))  # 不要漏掉逗号 因为args是一个元组,异步是可以有返回值的
        results.append(result)

    for res in results:
        print(res.get())

    # 如果主进程不阻塞,主进程会立即结束,导致进程池中的任务不会执行
    # 调用join之前,必须先调用close方法,调用close方法之后,能确保再继续添加新的任务了
    # 应该使用join方法,让主进程阻塞,等待进程池中的任务执行完毕后再结束
    # pool.close()
    # pool.join()
