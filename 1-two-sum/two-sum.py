from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           x=target-nums[i]
           if x in nums[:i]:
             return [nums.index(x),i]
           if x in nums[i+1:]:
             return [i,nums.index(x,i+1)]