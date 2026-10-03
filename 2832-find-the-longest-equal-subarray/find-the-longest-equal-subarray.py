class Solution:
    def longestEqualSubarray(self,nums:List[int],k:int)->int:
        dic={}
        left=0
        right=0
        max_freq=0
        ans=0
        while right<len(nums):
            dic[nums[right]]=dic.get(nums[right],0)+1
            if dic[nums[right]]>max_freq:
                max_freq=dic[nums[right]]
            if (right-left+1)-max_freq>k:
                dic[nums[left]]-=1
                left+=1
            else:
                ans=max(ans,right-left+1)
            right+=1
        return max_freq