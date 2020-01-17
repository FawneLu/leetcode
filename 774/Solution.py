```python
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        low=0
        high=stations[len(stations)-1]-stations[0]
        while low+1e-6<=high:
            count=0
            mid=low+(high-low)/2
            for i in range(len(stations)-1):
                count+=(stations[i+1]-stations[i])//mid
            if count>K:
                low=mid
            else:
                high=mid
        return low
```