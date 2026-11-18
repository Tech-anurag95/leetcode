class Solution:
    def minChanges(self, s: str) -> int:
        ans=0
        for i in range(0,len(s),2):
            if len(set(s[i:i+2]))==2:
                ans+=1
        return ans