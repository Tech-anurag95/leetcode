class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans=[]
        for num in nums:
            if num not in ans:
                ans.append(num)
        nums[:len(ans)]=ans
        return len(ans)