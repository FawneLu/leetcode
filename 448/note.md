- Tricky Way  
This is a tricky way which we can learn from the previous problem(645,setmismatch). We will apply reverse in this problem. If the number in the list isn't replicated, then we make the number multiply -1. Before this, we need to judge whether the number is smaller than 0. If so, means the number has been existed. Then we return the index which value is larger than 0.
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
