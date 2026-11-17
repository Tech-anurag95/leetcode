class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        ans=0
        count=0
        for cost in costs:
            ans+=cost
            if ans<=coins:
                count+=1
        return count
        