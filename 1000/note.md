### 动态规划
这道题好难啊。  
是一个dp问题， 首先我们要确定， 能拆分一个arry的话， 需要满足(n-1)%(k-1)==0。    
```python
for l in range(K,n+1):
            for i in range(n-l+1):
                j=i+l-1
                for m in range(i,j,K-1):
                    dp[i][j]=min(dp[i][m]+dp[m+1][j],dp[i][j])
                if (l-1)%(K-1)==0:
                    dp[i][j] += sums_[j + 1] - sums_[i]
```  
dp[i][j] 看的是i~j的cost。  我们在中间m的地方进行拆分， 左边分成1分， 右边不管几分， 是(k-1)的整数倍。  m每次加上k-1即可。