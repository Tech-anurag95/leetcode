class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        ans=0
        dis={}
        for num in nums:
            if num in dis:
                dis[num]+=1
            else:
                dis[num]=1
            ans=max(ans,dis[num])
        if ans>len(nums)-ans:
            return ans-(len(nums)-ans)
        else:
            return len(nums)%2