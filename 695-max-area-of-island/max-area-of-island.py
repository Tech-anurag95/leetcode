class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxarea=0
        visited=set()
        def connected(i,j):
            nonlocal area
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return
            if grid[i][j]==0 or (i,j) in visited:
                return
            visited.add((i,j))
            area+=1
            connected(i+1,j)
            connected(i-1,j)
            connected(i,j+1)
            connected(i,j-1)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1 and (x,y) not in visited:
                    area=0
                    connected(x,y)
                    maxarea=max(maxarea,area)
        return maxarea