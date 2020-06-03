class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left,right,up,down=0,n-1,0,n-1
        matrix=[[None]*n for _ in range(n)]
        num=1
        
        while left<=right and up<=down:
            for i in range(left,right+1):
                matrix[up][i]=num
                num+=1
            up+=1
            for i in range(up,down+1):
                matrix[i][right]=num
                num+=1
            right-=1
            for i in range(right,left-1,-1):
                matrix[down][i]=num
                num+=1
            down-=1
            for i in range(down,up-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
        
        return matrix