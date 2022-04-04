class Solution:
    def rob(self, nums: List[int]) -> int:
            return max(nums[0],self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
        
    def rob_helper(self, nums):
        rob1, rob2 = 0, 0
        for i in nums:
            rob1, rob2 = rob2, max(i + rob1, rob2)
        return rob2
        

        # 用rob1作为help func，分为两段，1.包括尾，没有头。2.有头无尾。取最大值