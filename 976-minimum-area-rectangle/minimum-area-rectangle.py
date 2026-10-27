class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s=set()
        for x,y in points:
            s.add((x,y))
        ans=float('inf')
        for x1,y1 in points:
            for x2,y2 in points:
                if x1<x2 and y1<y2:
                    if (x1,y2) in s and (x2,y1) in s:
                        area=(x2-x1)*(y2-y1)
                        ans=min(ans,area)
        return ans if ans!=float('inf') else 0