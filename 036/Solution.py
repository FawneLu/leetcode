class Solution:
    def isValidSudoku(board):
        n = len(board)
        visited = set()
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num != ".":
                    if num + " in row " + str(i) in visited or num + " in col " + str(j) in visited or num + " in cell " + str(i//3) + "-" + str(j//3) in visited:
                        return False
                    visited.add(num + " in row " + str(i))
                    visited.add(num + " in col " + str(j))
                    visited.add(num + " in cell " + str(i//3) + "-" + str(j//3))

        return True



    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidCell(board)
    
    def isValidRow(self,board):
        n=len(board)
        for r in range(n):
            row=[x for x in board[r] if x!='.']
            if len(set(row))!=len(row):
                return False
        return True
    
    def isValidCol(self,board):
        n=len(board)
        for c in range(n):
            col=[board[r][c] for r in range(n) if board[r][c]!='.']
            if len(set(col))!=len(col):
                return False
        return True
    
    def isValidCell(self,board):
        n=len(board)
        for r in range(0,n,3):
            for c in range(0,n,3):
                cell=[]
                for i in range(3):
                    for j in range(3):
                        num=board[r+i][c+j]
                        if num!=".":
                            cell.append(num)
                
                if len(set(cell))!=len(cell):
                    return False
        
        return True