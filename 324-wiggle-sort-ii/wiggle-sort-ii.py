class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        arr=sorted(nums)
        n=len(nums)
        ans=[0]*len(nums)
        for i in range(1,n,2):
            ans[i]=arr.pop()
        for i in range(0,n,2):
            ans[i]=arr.pop()
        nums[:]=ans

# we just need to pop from sorted array but first at odd indexes then at even indexes
# PHLE ODD THEN EVEN 