```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        dp=[[0]*(n2+1) for i in range(n1+1)]
        for i in range(n1):
            dp[i+1][0]=dp[i][0]+1
        for j in range(n2):
            dp[0][j+1]=dp[0][j]+1
        
        for i in range(n1):
            for j in range(n2):
                if str1[i]==str2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j])+1
        
        
        i,j=n1-1,n2-1
        res=""
        while i>=0 and j>=0:
            if str1[i]==str2[j]:
                res+=str1[i]
                i-=1
                j-=1
            elif dp[i+1][j+1]==(dp[i+1][j]+1):
                res+=str2[j]
                j-=1
            elif dp[i+1][j+1]==(dp[i][j+1]+1):
                res+=str1[i]
                i-=1
        
        if i<0:
            while j>=0:
                res+=str2[j]
                j-=1
        
        else:
            while i>=0:
                res+=str1[i]
                i-=1
        
        return res[::-1]
```