# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知
# 所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；
# 如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告
# 异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告
# 诉Python发生异常时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：
# 显示你编写的友好的错误消息，而不是令用户迷惑的traceback

# # 触发除零异常
# print(5 / 0)  # ZeroDivisionError: division by zero
# # ZeroDivisionError是一个异常对象，Python无法按照你的指示做时，就会创建这种对象


# # 使用try-except代码块
# 如果try代码块中的代码运行
# 起来没有问题，Python将跳过except代码块,如果有问题Python将查找
# 这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("other logic ...")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:  # 放入仅在try代码块成功运行时才需要执行的代码
        print(answer)
