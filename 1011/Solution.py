```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        high = sum(weights)
        low = max(high//D, max(weights))
        
        while low<=high:
            mid=(high+low)//2
            cursum=0
            days=1
            for w in weights:
                if cursum+w>mid:
                    days+=1
                    cursum=0
                cursum+=w
            if days>D:
                low=mid+1
            else:
                high=mid-1
        
        return low
```