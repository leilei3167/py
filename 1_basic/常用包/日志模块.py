# 日志格式
import logging
from logging import handlers

# 初始化日志配置
logging.basicConfig(
    level=logging.DEBUG,  # 日志级别
    format="[%(levelname)s] %(asctime)s %(filename)s line:%(lineno)d: %(message)s",  # 日志格式
    # 将会输出: 2019-01-01 12:00:00 test.py[line:10]INFO:hello world
    filename="test.log",  # 日志文件名
    filemode="w",  # 写入模式
)

# 如果想要将日志输出到控制台, 可以使用StreamHandler
console = logging.StreamHandler()
# console.setLevel(logging.DEBUG) # 被根logger设置的level覆盖了
console.setFormatter(
    logging.Formatter(
        "[%(levelname)s] %(asctime)s %(filename)s line:%(lineno)d: %(message)s"
    )
)
logging.getLogger().addHandler(console)  # 获取root logger, 并添加Handler


logging.info("hello world")
logging.error("这是一个错误")
logging.warning("这是一个警告")
logging.debug("这是一个调试信息")
logging.critical("这是一个严重错误")
