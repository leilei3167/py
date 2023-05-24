from typing import Optional


# 1.判断是否有环
# 2.找到这个入环的节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 用set
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next
        return None


# 快慢指针
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    # 相遇后再出发,fast一次只移动一个,再次和slow相遇时一定是入口
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None
