class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        row=[0]*m
        column=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:  
                    row[i]+=1   #hint1
                    column[j]+=1
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (row[i]>1 or column[j]>1):  #check if there is more than 1 server in that row or column
                    count+=1
        return count
