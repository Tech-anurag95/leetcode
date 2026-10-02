'''same number cannot appear twice in the same row. So if a number appears k times, you need at least k rows.
no of rows = max frequency of any element''' 

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        from collections import Counter
        k=max(Counter(nums).values())
        visited=[False]*len(nums)
        ans=[]
        for i in range(k):
            a=set()
            left=0
            while left<len(nums):
                if nums[left] not in a and visited[left]==False:
                    a.add(nums[left])
                    visited[left]=True
                left+=1
            ans.append(list(a))
        return ans


        