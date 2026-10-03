class Solution:
    def maximumLength(self,s:str)->int:
        n=len(s)
        ans=-1
        for i in range(n):
            for j in range(i,n):
                sub=s[i:j+1]
                if len(set(sub))!=1:
                    continue
                count=0
                for k in range(n-len(sub)+1):
                    if s[k:k+len(sub)]==sub:
                        count+=1
                if count>=3:
                    ans=max(ans,len(sub))
        return ans