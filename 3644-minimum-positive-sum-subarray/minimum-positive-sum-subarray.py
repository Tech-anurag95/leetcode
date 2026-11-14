class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        sums=[]
        start=0
        while start<n:
            end=start
            total=0
            while end<n:
                total+=nums[end]
                if l<=end-start+1<=r:
                    sums.append(total)
                end+=1
            start+=1
        ans=float("inf")
        for num in sums:
            if num>0:
                ans=min(ans,num)
        if ans==float("inf"):
            return -1
        return ans