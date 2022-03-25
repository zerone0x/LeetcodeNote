# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:

            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
                
#             分3情况
# 1. one bigger than root, one smaller than root. root
# 2. two bigger --> right
# 3. two smaller --> left