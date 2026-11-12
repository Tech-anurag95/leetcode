from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        q=deque()
        fresh=0
        def isrotten(x,y):
            nonlocal fresh
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if grid[x][y]!=1 or (x,y) in visited:
                return
            fresh-=1
            visited.add((x,y))
            q.append((x,y))
            grid[x][y]=2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:   
                    q.append((i,j))  #agar wo rotten hai to queue me dal denge
        time=0
        while q and fresh>0:
            for i in range(len(q)):
                x,y=q.popleft()
                isrotten(x+1,y)
                isrotten(x,y+1)
                isrotten(x-1,y)
                isrotten(x,y-1)
            time+=1
        if fresh==0:   #saare rotten bn gye 
            return time
        else:   #saare rotten nhi bn paye 
            return -1