class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left=0
        right=0
        total=0
        window=set()
        ans=0
        while right<len(nums):
            while nums[right] in window:
                window.remove(nums[left])
                total-=nums[left]
                left+=1
            window.add(nums[right])
            total+=nums[right]
            if right-left+1>k:
                window.remove(nums[left])
                total-=nums[left]
                left+=1
            if right-left+1==k:
                ans=max(ans,total)
            right+=1
        return ans