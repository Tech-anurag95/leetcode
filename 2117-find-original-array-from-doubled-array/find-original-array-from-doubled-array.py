from collections import Counter
class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        ans=[]
        if len(changed)%2==1:
            return []
        count=Counter(changed)
        changed.sort()
        for num in changed:
            if count[num]==0:    
                continue
            if count[num*2]==0:      #duplicate not available
                return []
            count[num]-=1
            count[num*2]-=1
            ans.append(num)
        return ans

