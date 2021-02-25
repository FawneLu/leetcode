class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        def cal_dis(left,right):
            total_dis = 0
            while left<right:
                total_dis += houses[right] - houses[left]
                left += 1
                right -= 1
            
            return total_dis
            
        houses.sort()
        cost = [[0] *len(houses) for _ in range (len(houses))] 
        for i in range(len(houses)-1):
            for j in range(i,len(houses)):
                cost[i][j] = cal_dis(i,j)
        
        
        dp = [[float('inf')]*(k+1) for _ in range(len(houses))]
        for i in range(len(houses)):
            dp[i][0] = 0
            dp[i][1] = cost[0][i]
            
        
        for i in range(1,len(houses)):
            for j in range(2,k+1):
                for m in range(i):
                    dp[i][j] = min(dp[i][j], dp[m][j-1]+cost[m+1][i])
        return dp[-1][-1]