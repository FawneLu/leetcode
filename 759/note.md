### 合并
这道题的思路是先排序然后合并两个两个集。  
```python
for i in intervals:
            if i.start<=pre.end and i.end>=pre.end:
                pre.end=i.end
            elif i.start>pre.end:
                res.append(Interval(pre.end,i.start))
                pre=i
```