- My Way  
This is the normal but maybe stupid way that I come up with. We use a loop to record the sum of two elements in the list. If the sum equals to the target, then we append the two indexs in a new list and then return this list.  
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
       
```
- Dictionary  
We use a dictionary to store the index and the number in the list. If the res(target-number) in the dictionary and the index of the res is not equal to the index then we return the two index. Otherwise, Dict[num]=index(We append the number in the dictionary).  
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
