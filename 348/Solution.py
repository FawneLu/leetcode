```python
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row, self.col ,self.dia1 ,self.dia2 ,self.n =[0]*n, [0]*n, 0, 0, n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player==1:
            mark=1
        else:
            mark=-1
        
        self.row[row]+=mark
        self.col[col]+=mark
        if row==col:
            self.dia1+=mark
        if row+col==self.n-1:
            self.dia2+=mark
        
        if self.n in self.row or self.n in self.col or self.n == self.dia1 or self.n == self.dia2:
            return (1)
        elif -self.n in self.row or -self.n in self.col or -self.n == self.dia1 or -self.n == self.dia2:
            return (2)
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
```