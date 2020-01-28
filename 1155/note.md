### 动态规划
看成一个骰子投掷d次。  
dp=[[0]* (target+1), for i in range(d)] 行表示投掷次数, 列表示投掷的和。  
dp[i][j] = sum(dp[i-1][k]), k>0 and j-k>0