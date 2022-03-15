

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        # l and r are index of array s
        while l < r:
            while l < r and not self.clear(s[l]):
                l += 1
            while l < r and not self.clear(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
            # pointer need move everycycle
        return True
        
    def clear(self, c):
        return c.isalnum() 
        # return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
        # python func 实现 == 高层封装