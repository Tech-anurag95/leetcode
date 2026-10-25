class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        count=0
        def isclosed(x,y):
            nonlocal closed
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return
            if grid[x][y]==1 or (x,y) in visited:
                return
            visited.add((x,y))
            if x==0 or y==0 or x==len(grid)-1 or y==len(grid[0])-1: #boundary elements can never be closed  
                closed=0   
            isclosed(x+1,y)
            isclosed(x,y+1)
            isclosed(x-1,y)
            isclosed(x,y-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 and (i,j) not in visited:
                    closed=1
                    isclosed(i,j)
                    if closed==1:
                        count+=1
        return count
# saare cell me jao 
# ensure they are not boundary cell
# agar boundary pe 0 mil gya to closed=0 and perform dfs
# if it is boundary cell then closed becomes 0 else it stays 1 and count+=1
