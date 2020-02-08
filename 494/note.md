### 动态规划
这道题用动态规划。  
dp[i][j] 表示前i个元素构成j的情况有几种。
可以在dp存储字典。  
dp[i+1][j-nums[i]]+=dp[i][j]
dp[i+1][j+nums[i]]+=dp[i][j] 