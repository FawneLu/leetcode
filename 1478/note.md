### 动态规划
dp[i][j] 表示在0~i个房子中插入j个mailbox。  
cost[i][j] 表示第i号房到j号房中插入一个mailbox的distance
dp[i][j] = min(dp[i][j],dp[m][j-1] + cost[m+1][i]), m为0~i-1中任意一个房  
The key of this problem is to solve a base case, optimally allocating one mailbox for houses[i~j], The intuition is to put the mailbox in the middle location, this only works if there are only tow houses, or all the houses are evenly distributed. The correct location is the “median position” of a set of houses. For example, if the sorted locations are [1,2,3,100], the average will be 26 which costs 146 while the median is 2, and the cost becomes 100.  

注意边界条件：  
for i in range(len(houses)):  
    dp[i][0] = 0  
    dp[i][1] = cost[0][i]  


计算i~j中插入一个mailbox的距离  
def cal_dis(left,right):
    total_dis = 0  
    while left<right:  
        total_dis += houses[right] - houses[left]  
        left += 1  
        right -= 1  
    
    return total_dis  