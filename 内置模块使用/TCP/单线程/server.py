import socket
import time

# 定义换行
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = """Hello! <h1>你好</h1>"""


# HTTP响应
response_params = '\r\n'.join(
    [
        'HTTP/1.0 200 OK',
        'Content-Type: text/plain; charset=utf-8',
        'Content-Length: {}\r\n'.format(len(body.encode())),
        body,
    ]
)


def handler(conn, addr):
    request = b""
    # 读取直到遇到结束符号
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    time.sleep(5)
    conn.send(response_params.encode())
    conn.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 8000))
    s.listen(5)
    print("开始监听")
    try:
        while True:
            # 单线程串行
            conn, addr = s.accept()
            handler(conn, addr)
    finally:
        s.close()


if __name__ == '__main__':
    main()
