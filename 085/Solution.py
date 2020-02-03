```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        
        heights=[0]*len(matrix[0])
        res=0
        
        for row in matrix:
            for j in range(len(matrix[0])):
                if row[j]=='0':
                    heights[j]=0
                else:
                    heights[j]+=1
            
            res=max(res,self.max_area(heights))
        
        return res
            
                    
        
        
    
    def max_area(self,heights):
        stack=[]
        heights.append(0)
        res=0
        for i in range(len(heights)):
            if not stack or heights[i]>heights[stack[-1]]:
                stack.append(i)
            
            while stack and heights[i]<=heights[stack[-1]]:
                index=stack[-1]
                stack.pop()
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                res=max(res,heights[index]*w)
            
            stack.append(i)
        
        return res
```