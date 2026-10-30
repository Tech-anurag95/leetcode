from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        currarea=float("-inf")
        while left<right:
            lambai=min(height[left],height[right])
            width=right-left
            area=lambai*width
            currarea=max(area,currarea)
            if (height[left]<height[right]):
                left+=1
            else:
                right-=1
        return currarea
                


       