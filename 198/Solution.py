```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,cur=0,0
        for num in nums:
            temp=prev
            prev=cur
            cur=max(temp+num,prev)
        
        return cur
```
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]
```