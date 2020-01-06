```python
class Solution:
    def nextClosestTime(self, time: str) -> str:
        time=time[:2]+time[3:]
        isValid = lambda t:int(t[:2])<24 and int(t[2:])<60
        stime=sorted(time)
        
        for x in (3,2,1,0):
            for y in stime:
                if y<=time[x]:continue
                ntime=time[:x]+y+stime[0]*(3-x)
                if isValid(ntime):
                    return ntime[:2]+':'+ntime[2:]
        return stime[0]*2+':'+stime[0]*2
```