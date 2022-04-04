# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        # 典型递归简单问题
        # return r and (setattr(r,'x',s.invertTree(r.left)) or setattr(r,'left',s.invertTree(r.right)) or setattr(r,'right',r.x) or r)
        
        
        # better code than above 
        # if root:
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root