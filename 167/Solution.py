```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        table={}
        for index,num in enumerate(numbers):
            res=target-num
            if res in table and table[res]!=index:
                return(min(index+1,table[res]+1),max(index+1,table[res]+1))
            else:table[num]=index
```  
```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=0
        high=len(numbers)-1
        while low<high:
            sum=numbers[low]+numbers[high]
            if sum==target:
                return(low+1,high+1)
            elif sum<target:
                low+=1
            else:
                high-=1
```