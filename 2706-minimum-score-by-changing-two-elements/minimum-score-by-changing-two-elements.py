class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1]-nums[2],  #smallest two removed
                   nums[-2]-nums[1],  #smallest and largest removed
                   nums[-3]-nums[0])  #largest two removed