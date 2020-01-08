```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances=[]
        for i,(x,y) in enumerate(workers):
            distances.append([])
            for j,(x_b,y_b) in enumerate(bikes):
                distance=abs(x-x_b)+abs(y-y_b)
                distances[-1].append((distance,i,j))
            distances[-1].sort(reverse=True)
        
        queue = [distances[i].pop() for i in range(len(workers))]
        heapq.heapify(queue)
        
        res=[None]*len(workers)
        used_bikes=set()
        while len(used_bikes)<len(workers):
            d,worker,bike=heapq.heappop(queue)
            if bike not in used_bikes:
                res[worker]=bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue,distances[worker].pop())
        return res
```