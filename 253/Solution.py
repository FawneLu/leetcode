```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[0])
        heap=[]
        for interval in intervals:
            if heap and interval[0]>=heap[0]:
                heapq.heapreplace(heap,interval[1])
            
            else:
                heapq.heappush(heap,interval[1])
        
        return (len(heap))
```

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals)==0:
            return 0
        
        time=[]
        for interval in intervals:
            time.append((interval[0],True))
            time.append((interval[1],False))
            
        time=sorted(time, key=lambda v:(v[0],v[1]))
        print(time)
        
        n=0
        max_num=0
        for t in time:
            if t[1]:
                n+=1
            else:
                n-=1
            max_num=max(max_num,n)
            
        return max_num
```