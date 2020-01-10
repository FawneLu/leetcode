### 动态规划
- 这道题比较tricky的地方是要用两个数组来储存不交换的次数和交换的次数。  
如果A[i]>A[i-1], B[i]>B[i-1], 对i位和i-1来说，为了保持合法，要么都不交换，要么都交换。 keep[i]=keep[i-1], swap[i]=swap[i-1]+1。  
接着我们再看，如果A[i]>B[i-1],B[i]>A[i-1], 我们可以交换i位也可以选择不交换。 结果取操作的最小值。 
keep[i]=min(swap[i-1],keep[i])  
swap[i]=min(keep[i-1],swap[i])  