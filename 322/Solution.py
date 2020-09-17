class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        INVALID = 10**10
        self.ans = INVALID
        def dfs(s, amount, count):      
            if amount == 0:
                self.ans = count
                return
            if s == len(coins): return
      
            coin = coins[s]
        
            for k in range(amount // coin, -1, -1):
                if count + k >= self.ans: break
                dfs(s + 1, amount - k * coin, count + k)
                
        dfs(0, amount, 0)
        return -1 if self.ans == INVALID else self.ans

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                if dp[i-coin]!=float('inf'):
                    dp[i]=min(dp[i],dp[i-coin]+1)
        
        return -1 if dp[amount]==float('inf') else dp[amount]
