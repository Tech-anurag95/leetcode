class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        count=0
        a={}
        for i in range(len(rectangles)):
            num=(rectangles[i][0]/rectangles[i][1])
            if num in a:
                a[num]+=1
            else:
                a[num]=1
        for value in a.values():
            count+= (value*(value-1))//2
        return count
            

        