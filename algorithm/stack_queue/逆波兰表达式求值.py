from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 定义字符对应的操作
        from operator import add, sub, mul
        op_map = {'+': add, '-': sub, "*": mul, "/": lambda x, y: int(x / y)}
        stack = []
        for token in tokens:
            # 不是操作符,则转换为整数后入栈
            if token not in op_map.keys():
                stack.append(int(token))
            else:
                # 取出两个栈顶做运算,注意,先出来的是右操作数
                right = stack.pop()
                left = stack.pop()
                stack.append(op_map[token](left, right))
        return stack.pop()
