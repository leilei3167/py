from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            t1 = cur.next
            # 保存下下个
            t2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = t1
            t1.next = t2
            cur = cur.next.next
        return dummy.next


class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 但凡是操作链表,都要找到其待操作节点的前一个位置,比如想要交换0,1两个索引的值,必须先找到-1的位置(没有的话一般通过构造dummy节点)
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            third = cur.next.next.next

            cur.next = second
            second.next = first
            first.next = third
            cur = cur.next.next
        return dummy.next
