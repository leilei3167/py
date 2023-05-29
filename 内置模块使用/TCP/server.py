import socket
import threading


def tcplink(sock, addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b"Welcome!")
    while True:
        data = sock.recv(1024)
        # time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("Hello, %s!" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Connection from %s:%s closed." % addr)


if __name__ == "__main__":
    # 创建一个基于IPv4和TCP协议的Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听地址和端口
    s.bind(("127.0.0.1", 9999))
    # 开始监听,指定最大等待连接数
    s.listen(5)
    print("Waiting for connection...")

    try:
        i = 0
        while True:
            sock, addr = s.accept()
            # 接收到一个连接就开启一个线程,否则无法同时处理多个连接
            t = threading.Thread(
                name='thread-%s' % i, target=tcplink, args=(sock, addr)
            )
            t.start()
    finally:
        s.close()
