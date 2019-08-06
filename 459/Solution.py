```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return false
        k=2
        while k<=len(s):
            if len(s)%k==0 and s[:len(s)//k]*k==s:
                return True
            k+=1
        return False
```
