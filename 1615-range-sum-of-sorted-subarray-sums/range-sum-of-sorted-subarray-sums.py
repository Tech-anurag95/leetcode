class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sums=[]
        l=0
        r=0
        total=0
        while l<n:
            total+=nums[r]
            sums.append(total)
            if r==n-1:
                l+=1
                r=l
                total=0
            else:
                r+=1
        sums.sort()
        return sum(sums[left-1:right])%(10**9+7)