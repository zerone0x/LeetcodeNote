class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)- 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

        # 类似decode，brute force是决策树。
        # 找和wordict里符合的string
        # 如果符合，那就把尾dp值赋给首dp值
        # 如果dp是true，就继续倒序遍历，如果是false，那就继续下一个word认证
        # 返回首dp值