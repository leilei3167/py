filename = "alice.txt"
try:
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


# 独立为函数
def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)  # 可以使用pass语句来处理,即什么都不会做
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = ["1.txt", "2.txt", "3.txt"]
for i in filename:
    count_words(i)
