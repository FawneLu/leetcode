```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        res=0
        pre=-1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if stack==[]:
                    pre=i
                else:
                    stack.pop()
                    if stack==[]:
                        res=max(res,i-pre)
                    else:
                        res=max(res,i-stack[len(stack)-1])
        return res
```

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)
        res=0
        for i in range(len(s)):
            
            if s[i]==')':
                if i>0 and s[i-1]=='(':
                    dp[i]=dp[i-2]+2

                if i>0 and s[i-1]==')':
                    if i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                        if i-dp[i-1]-1>0:
                            dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
                        else:
                            dp[i]=dp[i-1]+2

                res=max(res,dp[i])
        return res
```