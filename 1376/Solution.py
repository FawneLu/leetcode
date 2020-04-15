class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        layer=collections.defaultdict(set)
        self.res=0
        
        for i in range(n):
            layer[manager[i]].add(i)
        
        def dfs(i,time):
            if i in layer:
                for sub in layer[i]:
                    dfs(sub,time+informTime[i])
            
            else:
                self.res=max(self.res,time)
                return 
        
        dfs(headID,0)
        
        return self.res