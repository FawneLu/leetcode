```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        if len(s)==2:
            if s=='AA':
                return False
        for i in range(len(s)-1):
            if s[i]=='A':
                count+=1
                if count>=2:
                    return False
            if s[i:i+3]=='LLL':
                return False
        
        return True
```