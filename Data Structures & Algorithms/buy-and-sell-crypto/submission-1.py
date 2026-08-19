class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Maxprofit = 0
        l,r = 0,1 #left is buying and right is selling
        while r<len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                Maxprofit = max(Maxprofit, profit)
            else:
                l = r
            r +=1
        return Maxprofit