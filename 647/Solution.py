```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        dp=[[0]*n for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                dp[j][i]= (s[j] == s[i]) & ((i - j < 2) | dp[j+1][i-1])
                if dp[j][i]:
                    count+=1
            dp[i][i]=1
            count+=1
        
        return count
```