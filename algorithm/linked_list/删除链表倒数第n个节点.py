from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针,先让快指针先走n个节点,之后slow开始走,当快指针为None时,slow指针所在处就是要删除的节点
        # 所以应该让slow指针落在待删除指针的前一位
        dummy = ListNode(next=head)
        slow = fast = dummy
        # fast先走n+1
        for i in range(n + 1):
            fast = fast.next

        # 之后slow开始走,直到fast为空
        while fast:
            slow = slow.next
            fast = fast.next

        # 此时slow就是待删除节点前一个位置
        slow.next = slow.next.next

        return dummy.next
