```python
import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None]*n
        tmp = []
        for i in range(n-1, -1, -1):
            t = nums[i]
            pos = bisect.bisect_left(tmp, t)
            ans[i] = pos
            tmp.insert(pos, t)
            

        return ans
```