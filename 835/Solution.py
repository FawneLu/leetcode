```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N=len(A)
        LA=[(xi,yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
        LB=[(xi,yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
        d=collections.Counter([(x1-x2,y1-y2) for (x1,y1) in LA for (x2,y2) in LB])
        return max(d.values() or [0])
```