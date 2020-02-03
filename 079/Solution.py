```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(row,col,word):
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            if len(word)==0:
                return True
            
            if row<0 or row==len(board) or col<0 or col<0 or col==len(board[0]) or board[row][col]!=word[0]:
                return False
            
            board[row][col]='#'
            
            for dx,dy in directions:
                if backtracking(row+dx,col+dy,word[1:]):
                    return True
            
            board[row][col]=word[0]
            
        
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                if backtracking(i,j,word):
                    return True
        
        return False
```