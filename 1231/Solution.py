```python
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        low=1
        high=sum(sweetness)//(K+1)
        while low<=high:
            cursum=0
            cuts=0
            mid=low+(high-low)//2
            for s in sweetness:
                cursum+=s
                if cursum>mid:
                    cuts+=1
                    cursum=0
            if cuts>K:
                low=mid+1
            else:
                high=mid-1
                
        return low
```