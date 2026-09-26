class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if sum(nums[i:j+1]) in nums[i:j+1]:
                    count+=1
        return count+len(nums)
                    