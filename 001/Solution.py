```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
        return res
```  
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table={}
        for index,num in enumerate(nums):
            res=target-num
            if res in table and table[res]!=index:
                return(index,table[res])
            else:table[num]=index
```