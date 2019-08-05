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
```python
        nums.sort()
        if len(nums)<3 or nums[0]>1 or nums[-1]<0:
            return []
        
        result=[]
        for index,value in enumerate(nums):
            if value>0:
                break
            if index>0 and nums[index]==nums[index-1]:
                continue
            target=-value
            i,j=index+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j]<target:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                else:
                    result.append([nums[i],nums[j],value])
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                
                    i+=1
                    j-=1
        
        return result
```