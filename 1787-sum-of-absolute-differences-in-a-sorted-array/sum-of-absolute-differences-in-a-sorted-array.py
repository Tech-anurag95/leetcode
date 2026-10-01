class Solution:
    def getSumAbsoluteDifferences(self,nums:List[int])->List[int]:
        n=len(nums)
        total=sum(nums)
        ans=[]
        left_sum=0
        for i in range(n):
            left=i*nums[i]-left_sum
            right_sum=total-left_sum-nums[i]
            right=right_sum-(n-i-1)*nums[i]
            ans.append(left+right)
            left_sum+=nums[i]
        return ans