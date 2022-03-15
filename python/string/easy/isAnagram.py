class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(t) == sorted(s)
        # return Counter(t) == Counter(s)
        if len(s) != len(t):
            return False
        a, b = {}, {}
        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
            b[t[i]] = b.get(t[i], 0) + 1
        return a == b
        # hashmap存储字母和频率