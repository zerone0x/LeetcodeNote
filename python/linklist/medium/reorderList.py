# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
                        # fast.next 条件容易忽略
            slow, fast = slow.next, fast.next.next
        
        second = slow.next
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # reverse list
        
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = tmp1
            first.next = second
            first, second = tmp1, tmp2