class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nset = set(nums)
        
        for n in nums:
            if n-1 not in nset:
                length = 0
                while (n+length) in nset:
                    length += 1
                res = max(length, res)
        return res
    # 先把nums去重
    # 遍历nums，假如没有比当前值更小的，那当前值作为字符串的开头。
    # 每次当前值+1在set中找下一个，返回最大值