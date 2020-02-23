```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=float('-inf')
        pre_sum=[]
        pre_sum.append(0)
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        
        for i in range(len(pre_sum)-k):
            cum=pre_sum[i+k]-pre_sum[i]
            res=max(float(cum)/k,res)
        
        return res
```