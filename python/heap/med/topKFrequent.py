class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = 1 + count.get(i,0)
            
        for c, d in count.items():
            freq[d].append(c)
            
            
        res = []
        
        for i in range(len(freq)-1, 0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
# 将nums放在hashmap里。
# 初始化一个二维数组，来放map中的num的频率。

# 遍历freq中的每一个第一维，添加。
# 如果res等于k，返回。