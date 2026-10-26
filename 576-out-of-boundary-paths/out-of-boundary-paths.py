class Solution:
    def findPaths(self,m:int,n:int,maxMove:int,startRow:int,startColumn:int)->int:
        def boundary(x,y,moves):
            if x<0 or y<0 or x>=m or y>=n:
                return 1
            if moves==0:
                return 0         
            if (x,y,moves) in visited:
                return visited[(x,y,moves)]
            right=boundary(x+1,y,moves-1)
            left=boundary(x-1,y,moves-1)
            down=boundary(x,y-1,moves-1)
            up=boundary(x,y+1,moves-1)
            visited[(x,y,moves)]=(right+left+down+up)%(10**9+7)
            return visited[(x,y,moves)]
        visited={}
        return boundary(startRow,startColumn,maxMove)