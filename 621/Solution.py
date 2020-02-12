```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        new_task=[0]*26
        for t in tasks:
            new_task[ord(t)-ord('A')]+=1
        new_task.sort()
        i=25
        while i>=0 and new_task[i]==new_task[25]:
            i-=1
        
        len_frame=(new_task[25]-1)*(n+1)+(25-i)
        return max(len(tasks),len_frame)
```