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