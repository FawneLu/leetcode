class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0 / value
        ans = [self.dfs(x, y, table, set()) if x in table and y in table else -1.0 for (x, y) in queries]
        return ans
        
    def dfs(self, x, y, table, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in table[x]:
            if n in visited: continue
            visited.add(n)
            d = self.dfs(n, y, table, visited)
            if d > 0:
                return d * table[x][n]
        return -1.0