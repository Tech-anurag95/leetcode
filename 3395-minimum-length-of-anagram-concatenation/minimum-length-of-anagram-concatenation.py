from collections import Counter
class Solution:
    def minAnagramLength(self,s:str)->int:
        n=len(s)
        for k in range(1,n+1):
            if n%k!=0:
                continue
            freq=Counter(s[:k])
            valid=True
            for i in range(0,n,k):
                substring=s[i:i+k]
                if Counter(substring)!=freq:
                    valid=False
                    break
            if valid:
                return k