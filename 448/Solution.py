```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums:
            if nums[abs(i)-1]<0:
                continue
            else:
                nums[abs(i)-1]*=-1
        for i in range(0,len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
```  