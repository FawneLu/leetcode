```python3
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res=[1]
        while len(res)<=N:
            res=[2*i-1 for i in res]+[2*i for i in res]
        return [i for i in res if i<=N]
```