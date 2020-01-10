```python
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        cur=[i if x==T[0] else None for i,x in enumerate(S) ]
        for j in range(1,len(T)):
            last=None
            new=[None]*len(S)
            for i,u in enumerate(S):
                if last is not None and u==T[j]:
                    new[i]=last
                if cur[i] is not None:
                    last=cur[i]
            cur=new
        ans = 0, len(S)
        print(ans)
        print(cur)
        
        for e, s in enumerate(cur):
            if s is not None and e - s < ans[1] - ans[0]:
                ans = s, e
        
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""
```