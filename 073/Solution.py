class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
                
        
        
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        index_m = set()
        index_n = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_m.add(i)
                    index_n.add(j)
        
        
        for i in range(m):
            for j in range(n):
                if i in index_m or j in index_n:
                    matrix[i][j] = 0