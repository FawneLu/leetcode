class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        dic=collections.defaultdict(list)
        g=[0]*N
        
        for pre, next_c in relations:
            dic[pre-1].append(next_c-1)
            g[next_c-1]+=1
        
        q=collections.deque()
        
        reslen=0
        
        for i in range(N):
            if g[i]==0:
                q.append(i)
                reslen+=1
        
        res=0
        
        
        while q:
            n=len(q)
            
            for _ in range(n):
                c=q.popleft()
                
                for i in dic[c]:
                    g[i]-=1
                    if g[i]==0:
                        q.append(i)
                        reslen+=1
                        
            res+=1
        
        return res if reslen==N else -1