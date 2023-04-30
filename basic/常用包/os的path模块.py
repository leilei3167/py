import os

current = os.getcwd()
print(current)
new_path = "%s/test1" % current
file = "test.txt"
new_file_path = os.path.join(new_path, file)
print(new_file_path)

# exist 判断路径或文件是否存在
if os.path.exists(new_path):
    print("路径存在,打印其中的内容")
    print(os.listdir(new_path))
    if os.path.exists(new_file_path):
        print("文件存在,删除文件")
        os.remove(new_file_path)
    else:
        print("文件不存在,创建文件")
        f = open(new_path + "/%s" % file, "w")
        f.write("hello world")
        f.close()
else:
    print("路径不存在,创建路径")
    os.mkdir(new_path)

# isfile 判断是否是文件
print("是否是文件: ", os.path.isfile(new_file_path))
# isdir 判断是否是目录
print("是否是目录: ", os.path.isdir(new_path))
# isabs 判断是否是绝对路径
print("是否是绝对路径: ", os.path.isabs(new_path))


# join 路径字符串合并 通过/或\合并路径


# split 分割路径和文件名,返回元组
print("split直接分隔这个路径: ", os.path.split(new_file_path))
