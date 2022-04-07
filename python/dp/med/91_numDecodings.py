class Solution:
    def numDecodings(self, s: str) -> int:
        decode = { len(s) : 1}
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0": 
                decode[i] = 0
            else:
                decode[i] = decode[i+1]
        
            if (i+1 < len(s)  and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                # 注意两个条件用括号
                decode[i] += decode[i+2]
        return decode[0]
            
        # 和斐波那契相似在，它的每个值都来自之后值的和。
        # 后序遍历，每个值赋给前一个值。
        # 两个数的情况也很简单。但作为分支，需要加上两个数之后的cache值。
        # 返回第一个cache值。