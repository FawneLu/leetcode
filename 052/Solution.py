class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(k,j):
            for i in range(k):
                if board[i]==j or abs(board[i]-j)== abs(k-i):
                    return False
            return True
        
        def dfs(depth):
            if depth==n:
                self.res+=1
                return
            for i in range(n):
                if check(depth,i):
                    board[depth]=i
                    dfs(depth+1)
        
        board=[-1]*n
        self.res=0
        dfs(0)
        return  self.res