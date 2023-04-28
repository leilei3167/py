age = 19

# 注意,python使用缩进来表示代码块,属于同一个代码块的语句必须缩进相同的空格数
# if int(input("输入你的身高: ")) < 120:
#     print("身高不够")
# elif int(input("输入你的年龄: ")) < 18:
#     print("年龄不够")
# elif int(input("输入你的体重: ")) < 40:
#     print("体重不够")
# else:
#     print("恭喜你,可以进入游乐场")

# 嵌套使用

if int(input("输入你的身高: ")) > 120:
    print("身高大于120")
    if int(input("vip等级:")) > 3:
        print("vip等级大于3可以免费")
    else:
        print("vip等级小于3需要付费")
else:
    print("欢迎")
