```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        cur_sum=0
        for i,num in enumerate(nums):
            cur_sum+=num
            m=cur_sum%k if k else cur_sum
            if m not in d:
                d[m]=i
            elif d[m]+1<i:
                return True
        
        return False
```