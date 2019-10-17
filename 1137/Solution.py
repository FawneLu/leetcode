```python3
class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n):
            
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            res=helper(n-1)+helper(n-2)+helper(n-3)
            return res
        
        return helper(n)
```