class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            # 遍历s，如果有相同的值，remove左指针，并且左指针向右。
            # 如果没有相同的值，那就添加到s里
            
            res = max(res, r-l+1)
        return res
