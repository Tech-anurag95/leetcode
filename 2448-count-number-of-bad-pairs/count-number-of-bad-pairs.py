class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n=len(nums)
        goodpair=0
        d={}
        for i in range(len(nums)):
            if nums[i]-i in d:
                goodpair+=d[nums[i]-i]
                d[nums[i]-i]+=1
            else:
                d[nums[i]-i]=1
        return (n*(n-1))//2-goodpair