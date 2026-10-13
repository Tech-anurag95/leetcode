class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()   #taaki saare duplicates ek saath aa jayein
        def backtrack(start,subset):
            ans.append(subset.copy())
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans