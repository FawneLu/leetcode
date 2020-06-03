class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:return []
        
        m=len(matrix)
        n=len(matrix[0])
        
        left,right,up,down=0,n-1,0,m-1
        res=[]
        cur_d=0
        x,y=0,0
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        
        while len(res)!=m*n:
            res.append(matrix[x][y])
            if cur_d==0 and y==right:
                cur_d+=1
                up+=1
            elif cur_d==1 and x==down:
                cur_d+=1
                right-=1
            elif cur_d==2 and y==left:
                cur_d+=1
                down-=1
            elif cur_d==3 and x==up:
                cur_d+=1
                left+=1
            cur_d=cur_d%4
            x+=dirs[cur_d][0]
            y+=dirs[cur_d][1]
        
        return res