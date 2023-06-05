class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) < 1:
            return None
        return self.items[len(self.items) - 1]


# 使用栈来匹配括号
# 由空栈开始,遇到左括号即入栈,遇到右括号则出栈,处理完所有括号后栈必须是空的

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        # 左括号入栈
        if symbol == '(':
            s.push(symbol)
        else:
            # 当遇到右括号时,出栈,当遇到空栈时一定不匹配
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def parChecker1(symbolString):
    s = Stack()
    for i in symbolString:
        if i == '(':
            s.push(i)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()


# 扩展,匹配多种符号,如{()}[]这样是匹配的,({)[]}这样是不匹配的
def parChecker2(symbolString):
    s = Stack()
    for i in symbolString:
        # 左括号入栈
        if i in '{[(':
            s.push(i)
        else:
            # 右括号匹配的话则出栈
            if s.is_empty():
                return False
            else:
                # 和当前栈顶的对比
                top = s.pop()
                if not matches(top, i):
                    return False
    return s.is_empty()


def matches(left, right):
    lefts = "{[("
    rights = "}])"
    return lefts.index(left) == rights.index(right)


# 使用栈转化二进制
def divideBy2(decNumber):
    r = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        r.push(rem)  # 余数入栈
        decNumber = decNumber // 2  # 商

    # 二进制的顺序是倒序,从栈中依次取出
    binString = ''
    while not r.is_empty():
        binString += str(r.pop())

    return binString


# 转换为其他进制,如八进制和十六进制
# 转换为其他进制则是除以对应的进制基数
# 注意在10进制以内时,10个数字就足够,10进制以上时,余数都会是一个2位的十进制数,因此纯数字是不够的,需要一个方法表示大于9的余数
# 因此,将A设置为10,B设置为11以此类推

def baseConvert(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.is_empty():
        newString += str(digits[remstack.pop()])
    return newString


if __name__ == '__main__':
    print(parChecker("(())(())"))
    print(parChecker("())(())"))
    print(parChecker2("{[()]}"))
    print(parChecker2("{([)]}"))
    print(parChecker2("{}()[]"))
    print(parChecker2("{}[[(])]"))

    print(divideBy2(2))
    print(divideBy2(8))
    print(divideBy2(10))
    print(divideBy2(4096))
    print(divideBy2(7))

    print()
    tmp = 10086
    print(baseConvert(tmp, 10))
    print(baseConvert(tmp, 2))
    print(baseConvert(tmp, 8))
    print(baseConvert(tmp, 16))
