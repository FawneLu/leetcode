class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        t =s[::-1]
        if n == 0:
            return ""
        for i in range(n, 0 ,-1):
            if s[:i] == t[n-i:]:
                break
        
        return t[:n-i] + s