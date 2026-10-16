class Solution:
    def numIslands(self, grid:List[List[str]]) -> int:
        # matrix=[[False for j in range(n)]for i in range(m)]
        visited=set()
        count=0
        def isisland(x,y):
            if x<0 or y<0 or x>=len(grid) or y >=len(grid[0]):  #grid se bahar wali indexes
                return 
            if grid[x][y]=="0" or (x,y) in visited: #if the value is 0 or it is already visited
               return
            visited.add((x,y))   #visited me add kr do 
            isisland(x+1,y) #saari adjacent nodes ko check kro left,right,top,down 
            isisland(x,y+1)
            isisland(x-1,y)
            isisland(x,y-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):  #to check all points 
                if grid[i][j]=="1" and (i,j) not in visited:  #agar wo 1 hain aur not visited hain
                    count+=1 
                    isisland(i,j)   #aur iss vale pe function call kr do taki ye visted me add ho jaye aur tum adjacent indexes ko check kr sako
        return count
        
            
    #humara isisland function sirf 1 wali indexes ko seen me add krta hai
    #if i,j is 1 then i will go for other next indexes , agar wo already visited hain to move forward 


