class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        distinct=len(set(nums))
        right=0
        left=0
        while right<len(nums):
            if len(set(nums[left:right+1]))<distinct:
                right+=1
            else:
                count+=len(nums)-right
                left+=1
        return count