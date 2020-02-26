```python
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low=1
        high=m*n
        while low<=high:
            count=0
            mid=low+(high-low)//2
            for i in range(1,m+1):
                if i*n<=mid:
                    count+=n
                else:
                    count+=(mid//i)
                
            if count<k:
                low=mid+1
            else:
                high=mid-1
        return low
```