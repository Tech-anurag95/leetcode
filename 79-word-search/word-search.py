class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col: 
                return False
            if (r,c) in visited:
                 return False
            if board[r][c]!=word[i]:
                 return False
            visited.add((r,c))
            right=dfs(r,c+1,i+1)
            left=dfs(r,c-1,i+1) 
            down=dfs(r+1,c,i+1) 
            up=dfs(r-1,c,i+1)
            visited.remove((r,c))
            return right or left or down or up
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0): 
                    return True 
        return False
        
