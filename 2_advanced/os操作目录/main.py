# 实现dir -l输出


import os, time

tmp_path = os.path.abspath("./..")


# 打印指定目录的信息
def dir_list(pt: str):
    filenum, filesize, dirnum = 0, 0, 0
    for name in os.listdir(pt):
        n = os.path.join(pt, name)
        # 目录打印信息
        if os.path.isdir(n):
            print(
                "%s\t\t<DIR>\t\t%s"
                % (
                    time.strftime("%m-%d %H:%M", time.localtime(os.path.getmtime(n))),
                    name,
                )
            )
            dirnum += 1
        if os.path.isfile(n):
            print(
                "%s\t\t%d\t%s"
                % (
                    time.strftime("%m-%d %H:%M", time.localtime(os.path.getmtime(n))),
                    os.path.getsize(n),
                    name,
                )
            )
            filenum += 1
            filesize += os.path.getsize(n)
    print("\t\t%d个文件\t\t%d个字节" % (filenum, filesize))
    print("\t\t%d个目录" % dirnum)


# 在指定目录查找文件
def search(text, pt="."):
    res = []
    pt = os.path.abspath(pt)  # 替换为绝对路径
    # 如果是目录,则组装路径,递归搜索
    for name in os.listdir(pt):
        cur = os.path.join(pt, name)
        if os.path.isdir(name):  # 如果是目录,递归进入
            search(text, cur)
        elif name.find(text) != -1:
            res.append(cur)
    return res


if __name__ == "__main__":
    dir_list(tmp_path)
    print()
    print(search("12", tmp_path))
