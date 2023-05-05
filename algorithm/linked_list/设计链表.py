# 单链表节点类
class Node:
    def __init__(self, x=0):
        self.val = x
        self.next = None


# 链表
class MyLinkedList:
    def __init__(self):
        self.head = Node()  # 哨兵节点
        self.size = 0  # 便于操作

    # index从0开始,因此不可能到达size的大小
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        cur = self.head.next  # index=0时，cur指向第一个节点
        while index:
            cur = cur.next
            index -= 1  # 指针移动到index的位置
        return cur.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head.next  # 新节点指向原来的第一个节点
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        # 找到最后一个节点
        cur = self.head
        while cur.next:  # 循环结束时，cur指向最后一个节点
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        # 找到index的前一个节点
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return
        new_node = Node(val)
        pre = self.head  # 哨兵节点,相当于index=-1
        while index:
            pre = pre.next
            index -= 1
        new_node.next = pre.next
        pre.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1
