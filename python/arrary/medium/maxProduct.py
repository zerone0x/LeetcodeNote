class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i -1] * nums[i] > 0:
        #          nums[i] *= nums[i-1] 
        #     if nums[i -2] * nums[i] * nums[i-1] > 0:
        #         nums[i] = nums[i-2] * nums[i-1] * nums[i]
        #     res = max(res,nums[i])
        # return res
        maxP = max(nums)
        maxCurr, minCurr = 1, 1
        for n in nums:
            if n == 0:
                maxCurr, minCurr = 1, 1
                continue
            tmp = maxCurr
            maxCurr = max(maxCurr *n, minCurr * n, n)
            minCurr = min(tmp * n, minCurr * n, n)
            maxP = max(maxP, maxCurr)
        return maxP
        # 解决办法是找pattern
        # 1. nums是正数时，很容易解决
        # 2. 假如都是负数，那就需要在每一个index的地方
        # 留一个max和min
        # 再把正负数情况下的max和min列出。
        # 得把max或min的current数存一下，以防已经更新
        