class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount > max(coins):
        #     return -1
        # if amount == 0:
        #     return 0
        dp = (amount+1)*[amount + 1]
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-j])
                
        return dp[amount] if dp[amount] != amount+1 else -1
        
        # 遍历amount从0到最大值，每个值分解为所有的coin，如果不是-1，那就每次取它记录，遍历所有得到最小值。
        # 如果最后dp的值不等于初始化的值，那就返回dp。否则-1.