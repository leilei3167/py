# 在原有的Queue之上使用Manager封装一层,使得Queue可以通过网络被多个进程共享
import random, time, queue
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


# 将2个Queue都注册到网络上,callable参数关联了Queue对象
# 注意此处实际调用的是BaseManager的类方法(即classmethod),实际上是将Queue的创建方式存到了类中
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

# 实例化,设置服务器的ip地址和端口,并设置验证码
manager = QueueManager(address=("", 5000), authkey=b"abc")
manager.start()


# 注意,不要直接使用task_queue,而是通过manager.get_task_queue()获得的Queue接口
# 此处的get_task_queue方法是在register时被创建的
task = manager.get_task_queue()
result = manager.get_result_queue()


# 放任务

for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d..." % n)
    task.put(n)  # 任务队列
    time.sleep(1)


# 尝试接收结果

print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)  # 结果队列
    print("Result: %s" % r)


manager.shutdown()
print("master exit.")
