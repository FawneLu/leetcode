```python 
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals=sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res=[]
        pre=intervals[0]
        for i in intervals:
            if i.start<=pre.end and i.end>=pre.end:
                pre.end=i.end
            elif i.start>pre.end:
                res.append(Interval(pre.end,i.start))
                pre=i
        
        return res
```