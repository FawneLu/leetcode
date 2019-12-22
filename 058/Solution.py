```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        s=s.split(" ")
        index=-1
        while index!=-len(s)-1:
            if len(s[index])!=0:
                return len(s[index])
            index-=1
        return len(s[-1])
```