class Solution:
    def findUnsortedSubarray(self,nums:List[int])->int:
        n=len(nums)
        left=-1
        right=-1
        chota=float("inf")
        bda=float("-inf")
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                left=i
                break
        if left==-1:
            return 0
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                right=i
                break
        for i in range(left,right+1):
            chota=min(chota,nums[i])
            bda=max(bda,nums[i])
        while left>0 and nums[left-1]>chota:
            left-=1
        while right<n-1 and nums[right+1]<bda:
            right+=1
        return right-left+1