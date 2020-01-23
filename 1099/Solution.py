```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_res=-1
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]+A[j]<K:
                    max_res=max(max_res,A[i]+A[j])
        return max_res
```