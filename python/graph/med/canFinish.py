class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
            # 将每一个pre course添加到c的映射里
        visitset = set()
        # dfs前的set来检验是否存在过
        def dfs(c):
            if c in visitset:
                return False
            if premap[c] == []:
                return True
            visitset.add(c)
            
            for p in premap[c]:
                if not dfs(p):
                    # 递归检验本course的每一个pre course是否线性。
                    return False
            visitset.remove(c)
            premap[c] = []
            return True
        
        for c in range(numCourses):
            # 不要忘记写range
            if not dfs(c):
                return False
        return True
    # 遍历每一个course
    