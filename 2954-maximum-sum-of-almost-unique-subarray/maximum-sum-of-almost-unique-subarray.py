class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        left=0
        right=0
        ans=0
        total=0
        freq={}
        while right<len(nums):
            total+=nums[right]
            freq[nums[right]]=freq.get(nums[right],0)+1
            if right-left+1==k:
                if len(freq)>=m:
                    ans=max(ans,total)
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                total-=nums[left]
                left+=1
            right+=1
        return ans