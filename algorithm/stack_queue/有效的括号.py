class Solution:
    def isValid(self, s: str) -> bool:
        all_left = "({["
        all_right = ")}]"
        # 栈
        tmp = []
        for x in s:
            # 左边的全部入栈
            if x in all_left:
                tmp.append(x)
            elif len(tmp) == 0 and x in all_right:
                return False
            else:
                # 右边的和当前栈顶的对比
                cur = tmp[len(tmp) - 1]
                # 看是否匹配
                if all_left.index(cur) == all_right.index(x):
                    tmp.pop()
                else:
                    return False
        return len(tmp) == 0
