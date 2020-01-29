```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo={}
        def dp(i,j):
            if (i,j) not in memo:
                if j==len(p):
                    res=i==len(s)
                else:
                    first_match = i<len(s) and p[j] in {s[i],'.'}
                    
                    if len(p)>j+1 and p[j+1]=='*':
                        res=dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        res=first_match and dp(i+1,j+1)
                
                memo[i,j]=res
            return memo[i,j]
        
        return dp(0,0)
```
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p)>=2 and p[1]=='*':
            return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p)
        else:
            return self.isMatch(s[1:],p[1:]) and first_match
```