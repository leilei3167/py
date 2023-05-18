import random

num = random.randint(1, 100)

# while循环 while [condition]
count = 0
while count < 10:
    print(f"hello world,count: {count} ")
    count += 1

print("求1-100的和")
count = 0
sum = 0
while count <= 100:
    sum += count
    count += 1
print(f"1-100的和是{sum}")

# print("----------猜数字---------")
# flag = True
# c = 0
# while flag:
#     guess_num = int(input("请输入你猜的数字:"))
#     c += 1
#     if guess_num == num:
#         print("恭喜你猜对了")
#         flag = False
#     elif guess_num > num:
#         print("猜大了")
#     else:
#         print("猜小了")
# print("你一共猜了%d次" % c)

print("-------------9*9乘法表----------------")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}", end=" ")  # 使用end=" " 不换行
        j += 1
    print()
    i += 1
