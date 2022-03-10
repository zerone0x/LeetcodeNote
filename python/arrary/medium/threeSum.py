class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sumt = a + nums[l] + nums[r]
                if sumt < 0:
                    l += 1
                elif sumt > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return res
        # pattern --> 把index作为起点，右边第一个为left pointer，右边最后一个为right pointer。
        # 通过判断当前三个数的和与0的大小关系，来移动指针。
        # 当duplicate时候，就continue跳过。
        # 分两个地方: 1. 刚开始遍历。 2. sum为0时的重新开始