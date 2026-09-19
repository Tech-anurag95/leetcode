class Solution:
    def matrixReshape(self,mat:list[list[int]],r:int,c:int)->list[list[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        a=[]
        for i in range(m):
            for j in range(n):
                a.append(mat[i][j])
        ans=[]
        k=0
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(a[k])
                k+=1
            ans.append(row)
        return ans