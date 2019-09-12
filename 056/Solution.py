```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[]
        
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if interval[0]<=stack[-1][1]:
                    tmp=stack.pop()
                    stack.append([tmp[0],max(interval[1],tmp[1])])
                else:
                    stack.append(interval)
                    
        return stack
```
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        points=[]
        stack=[]
        res=[]
        for interval in intervals:
            points.append([interval[0],0])
            points.append([interval[1],1])
        
        points.sort()
        
        print(points)
        
        for point in points:
            if not point[1]:
                stack.append(point[0])
            else:
                start=stack.pop()
                if not stack:
                    res.append([start,point[0]])
        
        return res
```