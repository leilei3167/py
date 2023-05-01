# 异步可以直接获取返回值
# 异步的使用条件: 必须所有环境都是异步的,调用者和被调用者都必须是异步的

# async定义异步函数在def前使用
# await用于执行异步

import asyncio
import os
import random
import time


async def a():
    for i in range(10):
        print(i, "a is running on ", os.getpid())
        # time.sleep(random.random())  # cpu级别的阻塞,是阻塞的,被调用时,整个脚本都会被暂停,什么也做不了
        await asyncio.sleep(random.random())  # 非阻塞的,他会要求事件循环在等待这个语句完成的时候去执行其他内容
        # 这意味着使用 asyncio.sleep() 可以在等待期间继续执行其他任务，而使用 time.sleep() 则不能
    return "a function"


async def b():
    for i in range(10):
        print(i, "b is running on ", os.getpid())
        # time.sleep(random.random())
        await asyncio.sleep(random.random())
    return "b function"


# 定义一个异步函数的入口
async def main():
    t = time.time()
    result = await asyncio.gather(a(), b())
    print(result)
    print("total: ", time.time() - t)
    print("main pid: ", os.getpid())  # 异步和多进程不同,异步是在一个进程中执行的


# 主程序无法定义async,所以需要使用asyncio包调用异步函数 run_until_complete来执行异步函数
# gather 可以批量执行多个异步函数
# run执行单个异步函数
if __name__ == "__main__":
    asyncio.run(main())
