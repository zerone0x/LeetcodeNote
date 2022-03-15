class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            res += self.help(l, r, s)
            l, r = i, i + 1
            res += self.help(l, r, s)
        return res
    def help(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            res += 1
        return res