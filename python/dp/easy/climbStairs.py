# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n ==2:
#             return 2
#         if n >2:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one, two = one + two, tmp
        return one
    
# 斐波那契的变种。
# 倒序，one在倒数第二个，two在倒数第一个。range 为n-1
# 用普通recurse超时。
