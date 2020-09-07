class Solution:
    def numDecodings(self, s: str) -> int:
        self.dict = {}
        return self.helper(s)
    
    def helper(self,s):
        if len(s) == 0:
            return 1
        if s in self.dict:
            return self.dict[s]
        
        take_one, take_two = 0, 0
        
        if int(s[:1]) > 0 and int(s[:1]) <= 9:
            take_one = self.helper(s[1:])
        
        if int(s[:2]) >= 10 and int(s[:2]) <= 26:
            take_two = self.helper(s[2:])
            
        self.dict[s] = take_one + take_two
        
        return self.dict[s]
    
    def numDecodings1(self, s: str) -> int:
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            if i != 1 and "09"<s[i-2:i]<"27":
                dp[i] += dp[i-2]
        return dp[-1]