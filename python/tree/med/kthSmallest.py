# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0
        
        while curr and stack:
            while curr:
                stack.append(curr)
                # 将node放在stack中
                curr = curr.left
                
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            # 返回node的value
            curr = curr.right
                