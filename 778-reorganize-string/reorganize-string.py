from collections import Counter
class Solution:
    def reorganizeString(self,s:str)->str:
        count=Counter(s)
        ns=""
        prev=""
        while len(ns)<len(s):
            placed=False
            count=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
            for key,value in count.items():
                if key==prev or value==0:
                    continue
                ns+=key
                count[key]-=1
                prev=key
                placed=True
                break
            if not placed:
                return ""
        return ns