```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        if len(nums) < 3 or nums[-1] < 0 or nums[0] > 1: return []
        i=0
        res=[]
        while i<=len(nums)-3:
            if nums[i]>0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                i+=1
                continue
            count=-nums[i]
            left=i+1
            right=len(nums)-1
            while right>left:
                if nums[left]+nums[right]>count:
                    right-=1
                elif nums[left]+nums[right]<count:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                            
                    left+=1
                    right-=1
                        
            i+=1
        return res
```