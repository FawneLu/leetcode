class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board
        
        queue = collections.deque()
        for i in range(len(board)):
            if board[i][0] == "O":queue.append((i,0))
            if board[i][len(board[0])-1] == "O":queue.append((i,len(board[0])-1))
            
        for j in range(len(board[0])):
            if board[0][j] == "O":queue.append((0,j))
            if board[len(board)-1][j] == "O":queue.append((len(board)-1, j))
            
        while queue:
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            r,c = queue.popleft()
            board[r][c] = "N"
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == "O":
                    board[nr][nc] = "N"
                    queue.append((nr,nc))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "N":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"