class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m=len(board)
        n=len(board[0])
        count=0
        def check(i,j):
            count=0
            for x,y in [(i-1,j-1),(i-1,j),(i-1,j+1),
                        (i,j-1),(i,j+1),
                        (i+1,j-1),(i+1,j),(i+1,j+1)]:
                if 0<=x<m and 0<=y<n and abs(board[x][y])==1:
                    count+=1
            return count
        for i in range(len(board)):
            for j in range(len(board[0])):
                count=check(i,j)
                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j]=-1
                elif count==3:
                    board[i][j]=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
