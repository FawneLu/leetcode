```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s))==1:
            return s
        
        start,end=0,0
        
        def length(left,right):
            L=left
            R=right
            while L>=0 and R<len(s) and s[L]==s[R]:
                L-=1
                R+=1
            return R-L-1
        
        for i in range(len(s)):
            len1=length(i,i)
            len2=length(i,i+1)
            max_len=max(len1,len2)
            if max_len>end-start+1:
                start=i-(max_len-1)//2
                end=i+max_len//2
        return s[start:end+1]
```
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s))==1:
            return s
        dp=[[0]*len(s) for i in range(len(s))]
        start=0
        end=0
        maxlen=0
        
        # for i in range(len(s)):
        #     dp[i][i]=1
        
        for j in range(len(s)):
            for i in range(j):
                dp[i][j] = (s[j] == s[i]) & ((j - i < 2) | dp[i+1][j-1])
                if dp[i][j] and j-i+1>maxlen:
                    maxlen=j-i+1
                    start=i
                    end=j
            dp[j][j]=1
            
            
        return s[start:end+1]
```