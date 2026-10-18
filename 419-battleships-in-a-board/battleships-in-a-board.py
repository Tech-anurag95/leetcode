class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        connected=set()
        def battle(x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                return
            if board[x][y]=="." or (x,y) in connected:
                return
            connected.add((x,y))
            battle(x+1,y)
            battle(x-1,y)
            battle(x,y+1)
            battle(x,y-1)
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="X" and (i,j) not in connected:
                    count+=1
                    battle(i,j)
        return count