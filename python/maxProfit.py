class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxP = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxP = max(maxP, prices[j] - prices[i])
        # return maxP
        
        l, r = 0, 1 
        # 两个指针代替双层循环
        maxP = 0
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
                # 如果r值小的话，就把l移到r？
            r += 1
        return maxP
    
        # low = float('inf')
        # maxP = 0
        # for i in prices:
        #     maxP = max(maxP, i - low)
        #     low = min(i,low)
        # return maxP
        # 和上面一样，但l指针的对比直接用low来代替