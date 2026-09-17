class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(map(int, str(n)))
        l=len(nums)
        bp=l-2
        while bp>=0 and nums[bp]>=nums[bp+1]:
            bp-=1
        if bp==-1:
            nums.reverse()
            return -1
        i=l-1
        while nums[i]<=nums[bp]:
            i-=1
        nums[bp],nums[i]=nums[i],nums[bp]
        nums[bp+1:]=nums[bp+1:][::-1]
        num=int(''.join(map(str,nums)))
        if num>2147483647:
          return -1
        return num
        
        