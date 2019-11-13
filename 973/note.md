## 最大顶堆
- 对heapq来说，我们要维护最大顶堆最简单的方法就是把要添加的元素取负。
- 这道题要求最小值只需要维护一个最大顶堆就可以。
- 同时这道题要注意的是学会用lambda。
x=lambda item:
```python3
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis=lambda point:-(point[0]**2+point[1]**2)
        
        heap=[]
        for point in points:
            heapq.heappush(heap,(dis(point),point))
            if len(heap)>K:
                heapq.heappop(heap)
        return [item[1] for item in heap]
```