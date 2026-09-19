class Solution:
    def findLengthOfShortestSubarray(self,nums:list[int])->int:
        n=len(nums)
        left=0
        while left<n-1 and nums[left]<=nums[left+1]:
            left+=1
        if left==n-1:
            return 0
        right=n-1
        while right>0 and nums[right-1]<=nums[right]:
            right-=1
        ans=min(n-left-1,right)
        i=0
        j=right
        while i<=left and j<n:
            if nums[i]<=nums[j]:
                ans=min(ans,j-i-1)
                i+=1
            else:
                j+=1
        return ans