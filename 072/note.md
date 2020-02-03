### dp
这道题用dp解。 dp[i][j] 表示word1[0...i-1]和word2[0...j-1] 有几种解。  
我们需要考虑:  
if word1[i-1]==word2[j-1]:  
dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]-1)  
if not:  
dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])  

边界条件是:
dp[0][0]=0, dp[i][0]=i, dp[0][j]=j