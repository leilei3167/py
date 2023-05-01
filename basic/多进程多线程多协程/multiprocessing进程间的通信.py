import time
import json
import multiprocessing


class Work:
    def __init__(self, queue: multiprocessing.Queue):
        self.queue = queue

    # 向队列发送消息,注意,消息只能是字符串,因此要使用json.dumps()转换为字符串
    def send(self, msg: str):
        # 如果不是字符串类型,则转换为字符串
        if not isinstance(msg, str):
            msg = json.dumps(msg)
        self.queue.put(msg)

    # 一次发送20条信息
    def send_all(self):
        for i in range(10):
            self.send(str(i))
            time.sleep(1)

    # 接收消息 无限循环
    def receive(self):
        while True:
            js = self.queue.get()
            try:
                msg = json.loads(js)
            except:  # 不是json格式的字符串,直接打印
                msg = js
            print("received: ", msg)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    worker = Work(queue)  # 使用队列创建工作对象
    # 创建发送进程,发送一条消息
    send = multiprocessing.Process(
        target=worker.send, args=({"name": "zhangsan", "age": 18},)
    )
    send_all = multiprocessing.Process(target=worker.send_all)
    # 创建接收进程
    receive = multiprocessing.Process(target=worker.receive)
    receive.start()

    print("开始发送一条消息")
    send.start()
    time.sleep(1)
    print("开始发送10条消息")
    send_all.start()
    send_all.join()
    receive.terminate()  # 结束接收进程,执行到这一步说明发送已经全部发送完毕
