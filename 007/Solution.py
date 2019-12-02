```python3
class Solution:
    def reverse(self, x: int) -> int:
        res=0
        y=abs(x)
        while y!=0:
            a=y%10
            y=int(y/10)
            res=res*10+a
            #print(a,y)
            
        if (abs(res) > 2147483647):
            return 0
        if x<0:
            return -res
        else:
            return res
```
