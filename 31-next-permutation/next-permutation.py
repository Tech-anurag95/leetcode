class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        bp=n-2
        while bp>=0 and nums[bp]>=nums[bp+1]:
            bp-=1
        if bp==-1:
            nums.reverse()
            return
        i=n-1
        while nums[i]<=nums[bp]:
            i-=1
        nums[bp],nums[i]=nums[i],nums[bp]
        nums[bp+1:]=nums[bp+1:][::-1]
        return nums