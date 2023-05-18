try:
    print(5 / 0)
except Exception:  # 所有异常都是Exception的子类,代表捕获所有异常
    print("捕获到通用异常,但是过于宽泛,不建议使用")


# 捕获指定异常,或者多个exception指定异常
try:
    print(5 / 0)
except ZeroDivisionError as e:
    print("捕获到指定除零异常,并且打印异常信息:", e)
except FileNotFoundError as e:
    print("捕获到指定文件未找到异常,并且打印异常信息:", e)
else:
    print("没有异常时执行的代码")


# 或者使用元组指定多个异常
try:
    print(5 / 0)
except (ZeroDivisionError, FileNotFoundError, NameError) as e:
    print("捕获到指定异常,并且打印异常信息:", e)
else:
    print("没有异常时执行的代码")
