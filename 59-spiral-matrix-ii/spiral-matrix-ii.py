class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        row=n
        col=n
        a=[]
        srow=0
        erow=row-1
        scol=0
        ecol=col-1
        x=1
        matrix=[[0]*n for i in range(n)]
        while srow<=erow and scol<=ecol:
            for j in range(scol,ecol+1):
                matrix[srow][j]=x
                x+=1
            srow+=1
            for i in range(srow,erow+1):
                matrix[i][ecol]=x
                x+=1
            ecol-=1
            if srow<=erow:
                for j in range(ecol,scol-1,-1):
                    matrix[erow][j]=x
                    x+=1
                erow-=1
            if scol<=ecol:
                for i in range(erow,srow-1,-1):
                    matrix[i][scol]=x
                    x+=1
                scol+=1
        return matrix 