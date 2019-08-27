```python3
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res=""
        count=1
        i=len(S)-1
        while i>=0:
            if S[i]!='-':
                res=res+S[i]
                count+=1
                if count>K:
                    res=res+'-'
                    count=1
            i-=1
        
        return res[::-1].strip('-').upper()
```
