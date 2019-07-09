```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_c=0
        i=0
        for num in nums:
            if num==1:
                count+=1
            else:
                if count>max_c:
                    max_c=count
                count=0
        return max(max_c,count)
```  