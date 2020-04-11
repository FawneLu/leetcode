class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pre=[[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre[i][j]=pre[i][j-1]+pre[i-1][j]-pre[i-1][j-1]+mat[i-1][j-1]
        
        res, l=0, 0
        for i in range(m+1):
            for j in range(n+1):
                while i+l<=m and j+l<=n and pre[i+l][j+l]-pre[i+l][j]-pre[i][j+l]+pre[i][j]<=threshold:
                    res=l
                    l+=1
        
        return res