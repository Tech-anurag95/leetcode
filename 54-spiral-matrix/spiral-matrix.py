class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        a=[]
        srow=0
        erow=row-1
        scol=0
        ecol=col-1
        while srow<=erow and scol<=ecol:
            # for top row where row is fix but col changes
            for j in range(scol,ecol+1):
                a.append(matrix[srow][j])
            srow+=1  #ab humara new matrix ka starting row = rstart+=1
            # for right col where col is fix but row changes
            for i in range(srow,erow+1):
                a.append(matrix[i][ecol])
            ecol-=1 #ab humare new matrix ka col end=colend-1
            #  agar maan lo ek hi row hui to ??
            if srow<=erow:
                for j in range(ecol,scol-1,-1):
                    a.append(matrix[erow][j])
                erow-=1  #ek se jyada rows hain to humare new matrix ka end row=endrow-1
            #  agar ek hi col hua to 
            if scol<=ecol:
                for i in range(erow,srow-1,-1):
                    a.append(matrix[i][scol])
                scol+=1  #agar ek se jyada col hai to new column start = col start+1
        return a

