# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # p1, p2 = 0, 0
        # res = []
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # minlength = min(len(list1), len(list2))
        # while p1 < minlength and p2 < minlength:
        #     if list1[p1] < list2[p2]:
        #         res.append(list1[p1])
        #         p1 += 1
        #     else:
        #         res.append(list2[p2])
        #         p2 += 1
                        
        # return res
        # ---wrong above just try some scratch
        
        ## try to use recursion
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        # better than iteration below
        
        
        
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
    # dummy 头指针 
    