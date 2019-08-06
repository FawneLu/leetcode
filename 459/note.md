- 换个思路想问题
这道题不要去考虑怎么找重复的字符串，要考虑substring的重复次数。如果重复了k次，说明len（string）%k==0 并且s[:len(string)//k]*k==s。
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
