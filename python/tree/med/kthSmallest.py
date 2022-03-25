# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from cgitb import reset


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative
        # n = 0
        # stack = []
        # cur = root
        
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         # 将node放在stack中
        #         cur = cur.left
        #     cur = stack.pop()
        #     n += 1
        #     if n == k:
        #         return cur.val
        #     # 返回node的value
        #     cur = cur.right
                
        # recursive
        self.k = k 
        self.res = None
        self.help(root)
        return self.res
        
        def help(self, node):
            if not node:
                return 
            self.help(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return 
            self.help(node.right)