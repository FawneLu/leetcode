```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left=[]
        cum=0
        for num in nums:
            cum+=num
            sum_left.append(cum)
        
        sum_right=[]
        cum=0
        for num in nums[::-1]:
            cum+=num
            sum_right.append(cum)
        sum_right.reverse()
        
        for index,(x,y) in enumerate(zip(sum_left,sum_right)):
            if x==y:
                return index
        return -1
```
```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum_num=[]
        cum=0
        for num in nums:
            cum+=num
            cum_num.append(cum)
        for i,c in enumerate(cum_num):
            if c == (cum_num[-1] - c + nums[i]):
                return i
        return -1
```
