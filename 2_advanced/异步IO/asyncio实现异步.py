# asyncio的模型就是一个事件循环, 我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO

import asyncio


async def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = "GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % host
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()


async def main():
    async with asyncio.TaskGroup() as tg:
        for host in ["www.sina.com.cn", "www.sohu.com", "www.163.com"]:
            tg.create_task(wget(host))


asyncio.run(main())
