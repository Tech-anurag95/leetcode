from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
        # for i in range(len(nums)):
        #    x=target-nums[i]
        #    if x in nums[:i]:
        #      return [nums.index(x),i]
        #    if x in nums[i+1:]:
        #      return [i,nums.index(x,i+1)]