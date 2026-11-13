class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mincost=float("inf")
        profit=0
        for num in prices:
            mincost=min(mincost,num)
            if num>mincost:
                profit=max(profit,num-mincost)
        return profit

# if curr prices>mincost then profit=max(profit,num-mincost)
