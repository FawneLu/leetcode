```python
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heapmax=[]
        self.heapmin=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heapmax, -num)
        maxtop=self.heapmax[0] if len(self.heapmax) else None
        mintop=self.heapmin[0] if len(self.heapmin) else None
        if len(self.heapmin) and len(self.heapmax) and mintop < -maxtop:
            heapq.heappush(self.heapmin, -heapq.heappop(self.heapmax))
        elif 1<len(self.heapmax):
            heapq.heappush(self.heapmin, -heapq.heappop(self.heapmax))
        if len(self.heapmin)>len(self.heapmax):
            heapq.heappush(self.heapmax, -heapq.heappop(self.heapmin))
        
    def findMedian(self) -> float:
        if len(self.heapmin)==len(self.heapmax):
            return float((self.heapmin[0]-self.heapmax[0])/2)
        if len(self.heapmax)>len(self.heapmin):
            return -self.heapmax[0]
        
        

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums=[]

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)

#     def findMedian(self) -> float:
#         self.nums=sorted(self.nums)
#         n=len(self.nums)
#         if n%2!=0:
#             return self.nums[(n-1)//2]
#         else:
#             return float((self.nums[(n-1)//2]+self.nums[n//2])/2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```