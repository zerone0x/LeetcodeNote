class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prep = 1
        for i in range(len(nums)):
            res[i] *= prep
            prep *= nums[i]
        endp = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= endp
            endp *= nums[i]
        return res
    # 这个题的解决办法是将此index两边的product计算分开
    # 其实两个循环合并通过～来计算效率更高