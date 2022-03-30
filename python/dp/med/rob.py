class Solution:
    def rob(self, nums: List[int]) -> int:
        # res = 0
        # n = len(nums)
        # for i in range(nums):
        #     res = max(res, nums[i] + self.rob(nums[i+1 : n]))
        # return res
        rob1, rob2 = 0, 0
        for n in nums:
            # tmp = max(rob1+n, rob2)
            # rob1 = rob2
            # rob2 = tmp
            rob1, rob2 = rob2,max(rob1+n, rob2)
        return rob2
# 比较当前index的rob值和前1个的rob值大小。
# 当前值是n+rob1
# 前一个值是rob2