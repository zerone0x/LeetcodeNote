class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+ 1
            else:
                r = m-1
        return res
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l = m+1
        #     else:
        #         r = m
        # return nums[l]
#         binary search 
# 用res作cache 加速
# 每次都要留下最小值
# 迭代
