```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        return False
```

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        ini=x
        res=0
        while x>0:
            res=res*10+x%10
            x=x//10
       
        if res==ini:
            return True
        return False
```