# finally代表一定会执行的代码块,无论是否发生异常,即使try或except中有return,finally也会执行


def test():
    try:
        return 3 / 1
    except (IOError, ZeroDivisionError) as e:
        return f"except {e}"
    finally:
        print("finally代码块,一定会执行")
    # return "finally代码块,一定会执行"


# 多个return,最终会执行finally中的return
print(test())
