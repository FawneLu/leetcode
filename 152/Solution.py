```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=[0]*len(nums)
        mi=[0]*len(nums)
        mx[0],mi[0],res=nums[0],nums[0],nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]>0:
                mx[i]=max(mx[i-1]*nums[i],nums[i])
                mi[i]=min(mi[i-1]*nums[i],nums[i])
            else:
                t=mx[i-1]
                mx[i]=max(mi[i-1]*nums[i],nums[i])
                mi[i]=min(t*nums[i],nums[i])
                
            res=max(res,mx[i])
        
        return res
    
    def maxProduct1(self, nums: List[int]) -> int:
        mx=[0]*len(nums)
        mi=[0]*len(nums)
        mx[0],mi[0],res=nums[0],nums[0],nums[0]
        
        for i in range(1,len(nums)):
            mx[i]=max(mx[i-1]*nums[i],mi[i-1]*nums[i],nums[i])
            mi[i]=min(mx[i-1]*nums[i],mi[i-1]*nums[i],nums[i])
            res=max(res,mx[i])
        
        return res
```