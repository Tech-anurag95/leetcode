from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        q=deque()
        fresh=0
        def isisland(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if grid[x][y]!=1 or (x,y) in visited:
                return
            visited.add((x,y))
            grid[x][y]=2   #yha pe organge frsh tha use rotten kr diya 
            fresh_count[0]-=1       
            q.append((x,y))
        fresh_count=[0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh_count[0]+=1
        time=0
        while q and fresh_count[0]>0:
            for _ in range(len(q)):
                x,y=q.popleft()
                isisland(x+1,y)
                isisland(x,y+1)
                isisland(x-1,y)
                isisland(x,y-1)
            time+=1
        if fresh_count[0]==0:
            return time
        else:
            return -1