from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 求长度差值
        dis = self.getLength(headA) - self.getLength(headB)

        # 通过移动较长的链表，使两链表长度相等
        if dis > 0:
            # 移动a链表的头部
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))

        # 将两个头向前移动，直到它们相交
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 求两个长度
        len_a, len_b = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            len_a += 1

        cur = headB
        while cur:
            cur = cur.next
            len_b += 1

        # 比较长度,让较长的先走
        if len_a > len_b:
            step = len_a - len_b
            longer = headA
            shorter = headB
        else:
            step = len_b - len_a
            longer = headB
            shorter = headA

        # 让长的先走step
        while step:
            step -= 1
            longer = longer.next

        # 同时开始走,依次比较
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        return longer


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None

        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB

        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA
