### dp
dp[left][right]，表示区间left-->right的最优解（不包括，left和right 两个边界）  

nums[left] * nums[i] * nums[right]，表示最后一个被戳破的气球的得分，为什么要乘上两个边界值那？因为它是最后一个被戳破的气球，整体来看，最后就剩下一个，就是乘上两个1，在子区间内，就是乘上两边的边界值了。  

max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])，表示从区间内开始枚举i，计算出本次区间的最优解。  
