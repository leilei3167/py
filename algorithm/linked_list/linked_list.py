# 定义节点
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node()  # 哨兵节点,虚拟头结点
        self.size = 0  # 初始化长度为0,方便操作

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        to_add = Node(val)
        to_add.next = self.head.next
        self.head.next = to_add
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # 移动到末尾
        to_add = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = to_add
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return

        to_add = Node(val)
        # 移动到index前一个节点
        cur = self.head
        while index:
            index -= 1
            cur = cur.next
        to_add.next = cur.next
        cur.next = to_add
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        while index:
            index -= 1
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
