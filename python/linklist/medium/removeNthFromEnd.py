# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        Left, Right = dummy, head
        while n > 0 and Right:
            n -= 1
            Right = Right.next
        while Right: 
            Left = Left.next
            Right = Right.next
        Left.next = Left.next.next
        # delete the node
        return dummy.next
    # 如果用指针来解决，那不变的是两个指针的距离。
    # 所以问题就要在刚开始把距离控制好。
    