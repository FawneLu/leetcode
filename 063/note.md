### 动态规划
注意，在对第一行和第一列进行操作时，dp[i][0]=1的条件是dp[i-1]==1 and ob[i][0]=0。 证明到这个点有路可走。  
遍历矩阵时，遇到障碍就将抵达方式置为0。