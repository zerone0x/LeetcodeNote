# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sametree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        # 如果当前节点下不是sametree，将subtree分别很root tree的left和right递归进行比较。
    def sametree(self, t, s):
        if not s and not t:
            return True
        if s and t and t.val == s.val:
            return (self.sametree(t.left, s.left) and self.sametree(t.right, s.right))
        return False
    
    # subtree是一个递归问题。它的base choice是选择left or right to compare the subtree