class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        
        def dfs(start, k, com):
            if k == 0:
                res.append(com[:])
                return
                
            for i in range(start, n+1):
                com.append(i)
                dfs(i+1, k-1, com)
                com.pop()
                
        dfs(1, k, [])
        return res