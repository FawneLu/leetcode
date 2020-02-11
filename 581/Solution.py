```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums=sorted(nums)
        if sort_nums==nums:
            return 0
        i,j=0,len(nums)-1
        
        while i <len(nums) :
            if nums[i]!=sort_nums[i]:
                start=i
                break
            i+=1
        while j>=0:
            if nums[j]!=sort_nums[j]:
                end=j
                break
            j-=1
        
        #print(start,end)
        return end-start+1
```