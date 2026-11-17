from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=[]
        for num in nums:
            if num!=val:
                ans.append(num)
        nums[:len(ans)]=ans
        return len(ans)