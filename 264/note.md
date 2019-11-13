## Ugly number
我们先把1加入heap中，每次弹出heap中最小的元素再添加此元素的2倍，3倍，5倍，确保添加的数不在heap中。
弹出的第n次数就是我们要求的第n大的ugly number。
```python3
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