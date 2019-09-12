- 第一种
这道题有两种解法。第一种方法是，我们先把每一个小的区间按起点从小到大排序。如果栈为空，我们就把interval压入栈。然后我们比较interval的起点和上一个interval（即为stack里最后一个interval）的终点的大小。如果该起点比上一个终点小，我们就把上一个interval弹出栈，出栈的interval的起点为起点，终点为interval的终点和出栈的interval的终点中较大的那一个。
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
- 第二种
这道题的第二种解法，就是把每一个interval中的两个数分成起点和终点。起点为0，终点为1.然后再从小到大排序。如果遇到起点就压入栈，如果遇到终点且栈不为空则弹出栈。栈为空时，返回刚弹出的起点，和此时压入栈的终点。
这种方法可以看做起点和终点两两配对。（+ + — - + -）+看做起点，-看做终点。栈为空时的终点和在它之前最小的起点相匹配。
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

