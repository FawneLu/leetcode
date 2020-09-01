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

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.smaller = [0]*len(nums)
        
        def mergesort(enum):
            half = len(enum) // 2
            
            if half:
                left, right = mergesort(enum[:half]), mergesort(enum[half:])
                m, n = len(left), len(right)
                i, j = 0, 0
                while j < n or i < m:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        self.smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
                
            return enum
        
        
        mergesort(list(enumerate(nums)))
        return self.smaller