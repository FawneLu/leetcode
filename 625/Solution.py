```python
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a<2:
            return a
        res=0
        count=1
        for i in range(9,1,-1):
            while a%i==0:
                a/=i
                res+=count*i
                count*=10
        
        if a==1 and res<2**31:
            return res
        else:
            return 0
```