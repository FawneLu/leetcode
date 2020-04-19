from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @lru_cache(None)
        def dfs(d, x):
            if d + 2*x >= n:
                return sum(piles[d:])
            res = float("-inf")
            for i in range(1, 2*x+1):
                res = max(res, sum(piles[d:d + i]) - dfs(d + i, max(i, x)))
            return res
        return (sum(piles) + dfs(0, 1))//2
