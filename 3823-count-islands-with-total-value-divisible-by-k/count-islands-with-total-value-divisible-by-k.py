class Solution:
    def countIslands(self,grid:List[List[int]],k:int)->int:
        ans=0
        connected=set()
        def island(x,y):
            if x>=len(grid) or y>=len(grid[0]) or x<0 or y<0:
                return 0
            if grid[x][y]==0 or (x,y) in connected:
                return 0
            connected.add((x,y))
            right=island(x+1,y)
            left=island(x-1,y)
            up=island(x,y+1)
            down=island(x,y-1)
            return grid[x][y]+up+down+left+right
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and (i,j) not in connected:
                    total=island(i,j)
                    if total%k==0:
                        ans+=1
        return ans