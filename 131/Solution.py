```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return s
        res=[]
        
        def dfs(s, cur):
            if not s:
                res.append(cur[:])
                return 


            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    cur.append(s[:i])
                    dfs(s[i:],cur)
                    cur.pop()
        
        
        dfs(s,[])
        
        return res
```