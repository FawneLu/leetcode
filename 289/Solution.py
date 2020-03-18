class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        for i in range(m):
            for j in range(n):
                cnt=0
                for direction in directions:
                    dx=i+direction[0]
                    dy=j+direction[1]
                    if dx>=0 and dx<m and dy>=0 and dy<n and (board[dx][dy]==1 or board[dx][dy]==2):
                        cnt+=1
                
                if board[i][j] and (cnt>3 or cnt<2):
                    board[i][j]=2
                elif not board[i][j] and cnt==3:
                    board[i][j]=3
        
        for i in range(m):
            for j in range(n):
                board[i][j]=board[i][j]%2