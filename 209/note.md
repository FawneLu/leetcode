 - Two pointer
 We use two pointers to calculate the sum. If the sum< s then we move the last pointer. If the sum>=s, then we move the first pointer.  
```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        pre_sum=[]
        table={}
        cum=0
        count=len(nums)
        first=0
        last=0
       
        if sum(nums)<s:
            return 0
        while last<len(nums):
            while last<len(nums) and cum<s:
                cum+=nums[last]
                last+=1
            while cum>=s:
                cum-=nums[first]
                first+=1
            count=min(count,last-first+1)
        
        return count
```  