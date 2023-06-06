class MyQueue:

    def __init__(self):
        self.in_q = []
        self.out_q = []

    def push(self, x: int) -> None:
        # 入栈
        self.in_q.append(x)

    def pop(self) -> int:
        if len(self.out_q) == 0:
            self.out_q.extend(self.in_q[::-1])
            self.in_q = []
        return self.out_q.pop()

    def peek(self) -> int:
        if len(self.out_q) == 0:
            self.out_q.extend(self.in_q[::-1])
            self.in_q = []
        return self.out_q[len(self.out_q) - 1]

    def empty(self) -> bool:
        return len(self.in_q) == len(self.out_q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    q = MyQueue()
    for i in s:
        q.push(i)
    print("入栈完成")

    s0 = q.pop()
    print(s0 == 1)
    s1 = q.pop()
    print(s1 == 2)
