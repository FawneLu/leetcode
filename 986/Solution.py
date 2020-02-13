```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n=len(A)
        m=len(B)
        res=[]
        i,j=0,0
        while i<n and j <m:
            low=max(A[i][0],B[j][0])
            high=min(A[i][1],B[j][1])
            
            if low<=high:
                res.append([low,high])
            
            if A[i][1]<=B[j][1]:
                i+=1
            else:
                j+=1
        
        return res
```