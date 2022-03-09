class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum = nums[0]
        curr = 0
        for i in range(1,len(nums)):
            if curr < 0:
                curr = 0
            curr += i
            # 分两种情况，当nums中的数值<0时，两个选择，一个是把curr置为0，一个是停止。
            # >0时，只有一种选择，就是继续加。
            # 计算出所有可能性，cache里只存当前的最大值
            maxsum = max(maxsum, curr)
        return maxsum

        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i]+nums[i-1],nums[i])
        # return max(nums)