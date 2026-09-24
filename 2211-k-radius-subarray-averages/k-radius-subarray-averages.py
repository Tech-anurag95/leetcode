class Solution:
    def getAverages(self,nums:list[int],k:int)->list[int]:
        n=len(nums)
        a=[-1]*n
        size=2*k+1
        if size>n:
            return a
        total=0
        left=0
        right=0
        while right-left+1<size:
            total+=nums[right]
            right+=1
        total+=nums[right]
        a[k]=total//size
        while right+1<n:
            total-=nums[left]
            left+=1
            right+=1
            total+=nums[right]
            a[left+k]=total//size
        return a