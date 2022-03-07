class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []  
        # 双层循环，bruce  
        
        # for i in range(len(nums)):
        #     if target - nums[i] in nums[i+1:]:
        #         return [i, nums[i+1:].index(target - nums[i]) + i + 1]
        # 切片后的单层循环
        d = {}            
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m],i]
            d[n] = i