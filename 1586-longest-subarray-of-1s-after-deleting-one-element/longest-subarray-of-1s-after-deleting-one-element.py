class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        countzero=0
        ans=0
        left=0
        for r in range(len(nums)):
            if nums[r]==0:
                countzero+=1
            while countzero>1:
                if nums[left]==0:
                    countzero-=1
                left+=1
            ans=max(ans,r-left)
        return ans
    #     class Solution:
    # def longestSubarray(self, nums: list[int]) -> int:
    #     countzero=0
    #     ans=0
    #     left=0

    #     for r in range(len(nums)):
    #         if nums[r]==0:
    #             countzero+=1

    #         while countzero>1:
    #             if nums[left]==0:
    #                 countzero-=1
    #             left+=1

    #         ans=max(ans,r-left)

    #     return ans
        