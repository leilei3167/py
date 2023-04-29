# 使用threading模块创建线程

import threading
import requests


# 多线程要执行的任务
def download_file(url, filename):
    """下载文件"""
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)


# 需要下载的url列表,每个文件都开启一个线程去下载
urls = ["http://example.com/file1.txt", "http://example.com/file2.txt"]
filenames = ["file1.txt", "file2.txt"]

# 创建线程列表
threads = []
for url, filename in zip(urls, filenames):
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
