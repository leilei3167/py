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

weight = float(input("请输入体重(kg):"))
height = float(input("请输入身高(m):"))

bmi = weight / (height**2)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
else:
    print("严重肥胖")


# 嵌套使用

if int(input("输入你的身高: ")) > 120:
    print("身高大于120")
    if int(input("vip等级:")) > 3:
        print("vip等级大于3可以免费")
    else:
        print("vip等级小于3需要付费")
else:
    print("欢迎")
