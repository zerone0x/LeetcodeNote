# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # s1 --> recursion 
        # if not root:
        #     return 0
        # if root:
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        # s2 --> BFS
        # if not root:
        #     return 0
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level
        # 使用双端队列 
        # 将每层的节点放在一个level，将当层之下的左右子树全部
        # 最后计算level总数
        
        #s3 --> iteration
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    # 与s2类似，区别在将depth作为一个参数