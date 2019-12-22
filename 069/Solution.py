```python
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=1
        right=x
        while right>=left:
            mid=int(left+(right-left)//2)
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                left=mid+1
            
        return right
```