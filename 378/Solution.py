```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        if n==0:
            return 0
        res=[]
        for i in range(n):
            for j in range(n):
                heapq.heappush(res,matrix[i][j])
        for i in range(k-1):
            heapq.heappop(res)
        return  heapq.heappop(res)
    
    
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        if n==0:
            return 0
        low,high=matrix[0][0],matrix[n-1][n-1]
        while low<=high:
            mid=low+(high-low)//2
            count=0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j]<=mid:
                        count+=1
                    else:
                        break
                    
            if count<k:
                low=mid+1
            else:
                high=mid-1
        
        return low
```