class Solution:
    def minChanges(self, s: str) -> int:
        def check(st):
            if len(set(st))==1:
                return 0
            if len(st)==2:
                return 1
        ans=0
        for i in range(0,len(s),2):
            ans+=check(s[i:i+2])
        return ans