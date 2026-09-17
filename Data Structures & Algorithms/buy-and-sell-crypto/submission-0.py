class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #buy low sell high
        #profit = sell - buy

        maxProf = 0
        minBuy = prices[0]
        
        for sell in prices:
            maxProf = max(maxProf, sell - minBuy)
            minBuy = min(minBuy, sell)

        
        return maxProf