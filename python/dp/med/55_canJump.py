import numbers


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1 
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

        # 初始化的goal是当前末尾的最后一个number
        # 从倒数第2个开始遍历。如果当前值加上当前index无法达到goal，那就继续遍历
        # 如果可以达到，就更新goal为当前index。