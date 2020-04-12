class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        res=0
        for i in range(m):
            for j in range(n):
                if i and j and matrix[i][j]:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                res+=matrix[i][j]
        return res
    
    def countSquares1(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        pre=[[0]*(n+1) for _ in range(m+1)]
        
        res=0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]:
                    res+=1
                pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+matrix[i-1][j-1]
        
        for l in range(2,min(m,n)+1):
            for i in range(m-l+1):
                for j in range(n-l+1):
                    if pre[i+l][j+l]-pre[i+l][j]-pre[i][j+l]+pre[i][j]==l**2:
                        res+=1
        
        return res