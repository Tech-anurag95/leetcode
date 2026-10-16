class Solution:
    def solve(self, board: list[list[str]]) -> None:
        connected=set()
        def  surround(x,y):
            if x>=len(board) or y>=len(board[0]) or x<0 or y<0:
                return 
            if board[x][y]=="X" or (x,y) in connected:
                return 
            connected.add((x,y))
            surround(x+1,y)
            surround(x-1,y)
            surround(x,y+1)
            surround(x,y-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                     if board[i][j]=="O" :
                        surround(i,j)
        for i in range(len(board)):
          for j in range(len(board[0])):
              if board[i][j]=="O" and (i,j) not in connected:
                 board[i][j]="X"
                    

#function of surround is to add all those cordinates which has O
#first for loop :- add all boundary points to connected
#second for loop :- change all non boundary x to o 
            
            
        