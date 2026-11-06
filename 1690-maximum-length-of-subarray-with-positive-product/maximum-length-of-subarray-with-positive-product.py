class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        left=0
        negative=0
        first=-1
        ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                left=right+1
                negative=0
                first=-1
            else:
                if nums[right]<0:
                    negative+=1
                    if first==-1:
                        first=right
                if negative%2==0:
                    ans=max(ans,right-left+1)
                else:
                    ans=max(ans,right-first)
        return ans

# Traverse the array and maintain the count of negative numbers, the first negative index, and the current window's starting index.
# If zero occurs, reset the window; if the negative count is even, consider the entire window, otherwise exclude the first negative number.