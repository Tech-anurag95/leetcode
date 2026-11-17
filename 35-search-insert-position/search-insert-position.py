class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return -i