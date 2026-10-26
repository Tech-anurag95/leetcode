#MY ANSWER
class Solution:
    def countIslands(self,grid:List[List[int]],k:int)->int:
        ans=0
        total=0
        connected=set()
        def island(x,y):
            nonlocal total
            if x>=len(grid) or y>=len(grid[0]) or x<0 or y<0:
                return
            if grid[x][y]==0 or (x,y) in connected:
                return
            connected.add((x,y))
            total+=grid[x][y]
            island(x+1,y)
            island(x-1,y)
            island(x,y+1)
            island(x,y-1)
            return (total)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and (i,j) not in connected:
                    total=0
                    if(island(i,j)%k)==0:
                        ans+=1
        return ans

