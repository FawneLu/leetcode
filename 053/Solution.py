```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum=nums[0]
        max_sum=nums[0]
        for i in range (1,len(nums)):
            temp_sum=max(temp_sum+nums[i],nums[i])
            if temp_sum>max_sum:
                max_sum=temp_sum
        return max_sum
```