class Solution:
    def numberOfBoomerangs(self,points:list[list[int]])->int:
        ans=0

        for i in range(len(points)):
            count={}
            for j in range(len(points)):
                if i==j:
                    continue
                d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                count[d]=count.get(d,0)+1
            for x in count.values():
                ans+=x*(x-1)  #agar count=x to wo (x-1) ke saath boomerangs bna skta hai 
        return ans