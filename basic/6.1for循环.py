# for循环
# 基础语法: for [临时变量] in [待处理数据集] 从序列中取出元素，赋值给变量，然后执行语句，直到序列中的元素取完为止
name = "iamyoudady"
a_count = 0
for n in name:
    print(n, end=" ")
    if n == "a":
        a_count += 1

print(f'\n a的个数是{a_count}')

# range语法:
# 1.range(num) 获取0到num-1的整数序列,如输入5,则获取0,1,2,3,4
for i in range(5):
    print("range(5):", i)

# 2.range(num1,num2) 获取[num1,num2]的数组 不包含num2
for i in range(3, 9):
    print("range(3,9):", i)

# 3.range(num1,num2,step) 获取[num1,num2]的数组 不包含num2,每个元素直接间隔step
for i in range(3, 9, 2):
    print("range(3,9,2):", i)

print("循环外部访问i,是可以访问i的(最新的值),规范是不建议这么做的: ", i)

# for循环嵌套
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j * i}', end=" ")
    print()
