class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        bdagap=float("-inf")
        for i in range(1,len(nums)):
            difference=nums[i]-nums[i-1]
            bdagap=max(bdagap,difference)
        return bdagap
        