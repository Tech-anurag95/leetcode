class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        visited={}
        def increasing(x,y):
            if (x,y) in visited:
                return visited[(x,y)]
            up=0
            down=0
            left=0
            right=0
            if x>0 and matrix[x-1][y]>matrix[x][y]:
                up=increasing(x-1,y)
            if x<m-1 and matrix[x+1][y]>matrix[x][y]:
                down=increasing(x+1,y)
            if y>0 and matrix[x][y-1]>matrix[x][y]:
                left=increasing(x,y-1)
            if y<n-1 and matrix[x][y+1]>matrix[x][y]:
                right=increasing(x,y+1)
            count=1+max(up,down,left,right)
            visited[(x,y)]=count
            return count
        ans=0
        for i in range(m):
            for j in range(n):
                length=increasing(i,j)
                ans=max(ans,length)
        return ans