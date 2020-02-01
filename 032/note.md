### dp & stack
这题有两种做法，一种是用stack，一种是用dp。  
- dp  
dp 要分情况讨论，我们只看s[i]==')' 的情况。  
如果s[i-1]=='('就直接dp[i-2]+2  
如果s[i-1]==')' 就要判断s[i-dp[i-1]-1]=='('  
a. 如果i-dp[i-1]-1>0, 证明前面还有字串,  
dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2   
b. 如果前面没有字串  
dp[i]=dp[i-1]+2  

- stack  
把未匹配的左括号的index压入栈中。  
如果遇到'(' 就append, 遇到')' 先判断stack是否为空，是的话pre=i, 不是的话就pop。  pop后如果stack为空， len=i-pre  
不为空，len=i-stack[-1]
