class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = i
            else:
                return True
        return False
    # 和two sum一样，过于简单，不需多看

        
        # numSet = list(set(nums))
        # return not (len(numSet) == len(nums))
        # 利用set()的去重性
        
        # hashset = set()
        # for i in nums:
        #     if i in hashset():
        #         return True
        #     hashset.add(i)
        # return False