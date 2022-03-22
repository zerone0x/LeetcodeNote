from numpy import kaiser


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dir = {}
        res = 0
        l= 0
        for i in range(len(s)):
            dir[s[i]] = 1 + dir.get(s[i], 0)
            
            if i-l+1 - max(dir.values()) > k:
                
                dir[s[l]] -= 1
                l +=1
            res = max(res, i-l+1)
        return res
    # 利用hashmap来存储频率和值
    # 遍历string，更新hashmap
    # 如果当前窗口长度和出现频率最高的值的差大于k，那就将窗口右移。左指针+1
    # 更新result