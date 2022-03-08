# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from secrets import choice


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return head
        # ---
        # recuse below
        # ---
        
        # if not head or not head.next:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head        
        
        # ---
        # base choice --> 分解为头节点和后面的两个节点.
        # 然后从最后面的这三个节点递归到最前面