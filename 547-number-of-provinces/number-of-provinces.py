class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected=set()
        count=0
        def dfs(x):
            connected.add(x)
            for i in range(len(isConnected)):
                if isConnected[x][i]==1 and i not in connected:
                    dfs(i)
        for j in range(len(isConnected)):
            if j not in connected:
                dfs(j)
                count+=1
        return count
        
#ADJACENCY MATRIX IS GIVEN 
      
