class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m-1):
            newrow = [1] * n
            for j in range(n-2, -1,-1):
                
                newrow[j] = newrow[j+1] + row[j]
            row = newrow
        return row[0]
# 倒推
# 两个方向，横向最后row都是1，向上，当前是下和右的和。
# 遍历除了最后row的所有row
# 遍历当前row的所有column，每一个当前值都是下和右的和。
# 然后更新row
# 最后返回row[0] --> 起点