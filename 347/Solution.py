```python3
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums).most_common(k)
        print(counter)
        res=[]
        for i in range(0,k):
            res.append(counter[i][0])
        return res
```
```python3
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter=Counter(nums)
        sorted_counter=sorted(counter.items(),key=lambda x:x[1], reverse=True )
        res=[]
        for i in range(k):
            res.append(sorted_counter[i][0])
        return res
```