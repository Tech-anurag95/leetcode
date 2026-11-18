class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=sum(nums)
        n=len(nums)
        return (n*(n+1)//2)-ans