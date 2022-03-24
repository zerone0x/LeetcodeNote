from numpy import column_stack


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visit, height):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or heights[r][c] < height:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows- 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols -1])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res
        
        # dfs --> 判断两边最大和最小的边界值。并且没被访问过。而且大于起点height。
        # 参数 
        # 1. 坐标
        # 2. visit 
        # 3. 比较值
        
        # 假设 m * n 
        # 遍历列 column
        # 1. 起点值 (0，c) 或 (n，c）
        # 反之
        # （r，0）或（r,m)
        