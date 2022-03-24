"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from lib2to3.pytree import Node


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        res = {}
        def dfs(node):
            if node in res:
                return res[node]
            copy = Node(node.val)
            res[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
        
        # 没看懂题，代码比较简单。
        # hashmap来存放node。一个old to new的映射。
        # 如果不在map里，就放到copy里。
        # 再将neighbors遍历，加到copy。递归neibors的Node