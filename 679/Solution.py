```python
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums)==1 and abs(nums[0]-24)<0.001:
            return True
        for i in range (len(nums)):
            for j in range (len(nums)):
                if i!=j:
                    base=[nums[k] for k in range(len(nums)) if k!=j and k!=i]
                    if self.judgePoint24(base+[nums[i]+nums[j]]):return True
                    if self.judgePoint24(base+[nums[i]*nums[j]]):return True
                    if self.judgePoint24(base+[nums[i]-nums[j]]):return True
                    if self.judgePoint24(base+[nums[j]-nums[i]]):return True
                    if nums[i] and self.judgePoint24(base+[nums[j]/nums[i]]):return True
                    if nums[j] and self.judgePoint24(base+[nums[i]/nums[j]]):return True
        return False
```