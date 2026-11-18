class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        degree=max(dic.values())
        ans=len(nums)
        for ele,value in dic.items():
            if value==degree:
                m=nums.index(ele)
                n=len(nums)-1-nums[::-1].index(ele)
                ans=min(ans,n-m+1)
        return ans