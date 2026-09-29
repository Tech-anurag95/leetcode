class Solution:
    def minDeletions(self, s: str) -> int:
        dic={}
        for num in s:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        arr=list(dic.values())
        used=set()
        count=0
        for freq in arr:
            while freq>0 and freq in used:
                freq-=1
                count+=1
            used.add(freq)
        return count
        