import hashlib
from functools import partial


def calculate_md5(filename: str, chunk_size=4096):
    md5_obj = hashlib.md5()
    # 二进制形式读取文件
    with open(filename, "rb") as f:
        # 等价,iter的第一个参数必须是一个对象,用于创建迭代器对象。它可以用于迭代可迭代对象（如列表、字符串、字典等）或自定义对象
        # 如果iter没有第二个参数时,则第一个参数必须是可迭代对象
        # 如果有第二个参数时,第一个参数必须是一个可调用对象(如不带参数的函数),这种情况下返回的迭代器,每次迭代都会调用这个函数(不带参数),如果
        # 此函数返回的是第二参数的值,则会停止迭代

        # for chunk in iter(lambda: f.read(chunk_size), b''):
        #     md5_obj.update(chunk)

        # 注意 b''相当于go中的io.EOF
        for chunk in iter(partial(f.read, chunk_size), b""):
            md5_obj.update(chunk)
    return md5_obj.hexdigest()


file_name = "./test.txt"

if __name__ == "__main__":
    m = calculate_md5(file_name)
    print(m)
