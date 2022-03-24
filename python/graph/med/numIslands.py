import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # 初始化判断
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))     
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for a,b in directions:
                    r, c = row+a,col+b
                    if(r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    island +=1
        return island
    
        # bfs --> 
        # 遍历每一个单元，如果没有被访问过，并且是1，bfs一下，再加一。
        