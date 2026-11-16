class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans=[]
        jyada=max(candies)
        for num in candies:
            if num+extraCandies>=jyada:
                ans.append(True)
            else:
                ans.append(False)
        return ans 