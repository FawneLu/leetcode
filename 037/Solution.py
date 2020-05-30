class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board=board
        self.solve()
        
    def solve(self):
        row,col=self.findempty()
        if row==-1 and col==-1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.issafe(row,col,num):
                self.board[row][col]=num
                if self.solve():
                    return True
                self.board[row][col]="."
        
        return False
    
    def findempty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col]==".":
                    return row,col
        
        return -1,-1
    
    def issafe(self,row,col,ch):
        boxrow=row-row%3
        boxcol=col-col%3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow,boxcol,ch):
            return True
        return False
    
    def checkrow(self,row,ch):
        for col in range(9):
            if self.board[row][col]==ch:
                return False
        return True
    
    def checkcol(self,col,ch):
        for row in range(9):
            if self.board[row][col]==ch:
                return False
        return True
    
    def checksquare(self,row,col,ch):
        for r in range(row,row+3):
            for c in range(col,col+3):
                if self.board[r][c]==ch:
                    return False
        return True