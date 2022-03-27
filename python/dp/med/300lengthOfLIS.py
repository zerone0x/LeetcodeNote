class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LST = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums) ):
                if nums[j] > nums[i]:
                    LST[i] = max(LST[i], LST[j] + 1)
        return max(LST)
    
    # recurse 
    # 按照tree来进行分支。如果下一个数小于当前最后一个，那就end。不再增加。
    # 刚开始每个可能性都是1
    # 从尾部开始遍历，保证后面的cache存在，不断递归到前面。
    
    # 很有意思的题