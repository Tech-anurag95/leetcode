class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums==sorted(nums):
           return 0
        if nums==sorted(nums)[::-1] and len(set(nums))>1:
           return len(nums)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                left=i
                break
        for j in range(len(nums)-1,0,-1):
           if nums[j]<nums[j-1]:
               right=j
               break
        chota=min(nums[left:right+1])
        bda=max(nums[left:right+1])
        while left>0 and nums[left-1]>chota:
            left-=1
        while right<len(nums)-1 and nums[right+1]<bda:
            right+=1
        return right-left+1

        
        
        
        
        