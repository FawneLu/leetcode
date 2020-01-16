```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n=len(workers)
        m=len(bikes)
        dis=[[0 for i in range(m)] for i in range(n)]
        
        for w,worker in enumerate(workers):
            wx,wy=worker[0],worker[1]
            for b,bike in enumerate(bikes):
                bx,by=bike[0],bike[1]
                dis[w][b]=abs(wx-bx)+abs(wy-by)
        
        def findres(w,usedbikes):
            if w>=n:
                return 0
            
            state=(w,tuple(sorted(list(usedbikes))))
            if state in dp:
                return dp[state]
            else:
                tmp=float('inf')
                for i in range(m):
                    if i not in usedbikes:
                        usedbikes.add(i)
                        t=dis[w][i]+findres(w+1,usedbikes)
                        usedbikes.remove(i)
                        tmp=min(t,tmp)
                dp[state]=tmp
            return tmp
        
        dp={}
        usedbikes=set()
        
        res=findres(0,usedbikes)
        return res
```