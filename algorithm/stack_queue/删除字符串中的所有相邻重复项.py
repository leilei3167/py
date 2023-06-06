class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ss = list(s)
        # 入栈
        for i in ss:
            if len(stack) > 0 and i == stack[-1]:
                # 和栈顶的比较
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
