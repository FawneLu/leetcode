```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res=["0"]*n
        size=k**n
        visited=set()
        visited.add("".join(res))
        
        def dfs(res,visited,size,k,n):
            if len(visited)==size:
                return True
            node="".join(res[len(res)-n+1:])
            for i in range(k):
                node+=str(i)
                if node not in visited:
                    res.append(str(i))
                    visited.add(node)
                    if dfs(res,visited,size,k,n):
                        return True
                    res.pop()
                    visited.remove(node)
                node=node[:-1]
        
        if dfs(res,visited,size,k,n):
            return ("".join(res))
        return ""
```