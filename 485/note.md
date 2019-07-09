- 为什么我这么笨！！！  
这道题就是....算了，自己反思一下为什么这么简单的你一开始没写出来吧.  
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