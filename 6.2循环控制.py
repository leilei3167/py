# continue 中断本次循环，继续下一次循环
for i in range(10):
    if i % 2 == 0:  # 跳过偶数
        continue
    print("continue跳过偶数:", i)

# break 中断整个循环，不再执行循环体中的其他语句
for i in range(10):
    if i == 5:  # 跳过偶数
        break
    print("还没遇到break:", i)

# break和continue都只能作用于所在的循环,对于外层的循环没有任何影响

for i in range(10):
    for j in (1, 2, 3, 4):
        if j == 4:
            break
        print("break只能中断所在循环:", i, j)

# 只能使用标志变量来中断外层循环
print()
print("使用标志变量来中断外层循环")
shoud_break = False
for i in range(10):
    for j in range(1, 10):
        if j == 7:
            shoud_break = True
            print("设置标志变量为True,break内层循环")
            break
        print("i,j:", i, j)
    if shoud_break:
        print("跳出外层循环")
        break
