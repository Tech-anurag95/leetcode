class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total=[]
        for num in wall:
            ans=0
            for each in num[:-1]:
                ans+=each
                total.append(ans)
        dic={}
        for num in total:
            dic[num]=dic.get(num,0)+1
        jyada=max(dic.values(),default=0)
        return len(wall)-jyada

