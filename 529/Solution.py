class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board,i,j):
            if board[i][j] != "E":
                return
            mine_count = 0
            directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
            for d in directions:
                dr = i + d[0]
                dc = j + d[1]
                if dr >= 0 and dr < len(board) and dc >= 0 and dc < len(board[0]) and board[dr][dc]== "M":
                    mine_count += 1
                        
            if mine_count == 0:
                board[i][j] = "B"
            else:
                board[i][j] = str(mine_count)
                return 
            
            for d in directions:
                dr = i + d[0]
                dc = j + d[1]
                if dr >= 0 and dr < len(board) and dc >= 0 and dc < len(board[0]):
                    dfs(board, dr, dc)
            
            
            
        if not board or not board[0]:
            return []
        i,j = click[0],click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        
        dfs(board, i, j)
        
        return board