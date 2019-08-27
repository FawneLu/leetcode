- 只差一点点
The tricky thing of this question is that we nned to leave the first part of letters which length is smaller than K alone. So we need to consider it from the tail of our string. We set K letters togther and add a dash between each parts.
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
