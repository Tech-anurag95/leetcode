
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        pivot=None
        for i in range(-2,-n-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot is None:
            nums.reverse()
            return
        for j in range(-1,pivot,-1):
            if nums[j]>nums[pivot]:
                nums[j],nums[pivot]=nums[pivot],nums[j]
                break
        nums[pivot+1:]=reversed(nums[pivot+1:])

