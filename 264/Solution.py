```python3
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        count=1
        while count<=n:
            target=heapq.heappop(heap)
            if target*2 not in heap:
                heapq.heappush(heap,target*2)
            if target*3 not in heap:
                heapq.heappush(heap,target*3)
            if target*5 not in heap:
                heapq.heappush(heap,target*5)
            count+=1
        return target
```