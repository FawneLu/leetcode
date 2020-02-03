```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==1:
            return nums
        
        left,right=0,len(nums)-1
        cur=0
        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left]=nums[left],nums[cur]
                left+=1
                cur+=1
            
            elif nums[cur]==1:
                cur+=1
            
            elif nums[cur]==2:
                nums[cur],nums[right]=nums[right],nums[cur]
                right-=1
```
```python
class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        
        count=collections.Counter(nums)
        if count[0]:
            for i in range(count[0]):
                nums[i]=0
        
        if count[1]:
            for j in range(count[0],count[0]+count[1]):
                nums[j]=1
        
        if count[2]:
            for k in range(count[1]+count[0],count[1]+count[0]+count[2]):
                nums[k]=2
```