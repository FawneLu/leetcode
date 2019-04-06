- Normal Way 
When we deal with subarray we need to think of preffix sum. We use a dictionary to record the preffix sum and their number.     
```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table={0:1}
        cum=0
        count=0
        for num in nums:
            cum+=num
            if cum-k in table:
                count+=table[cum-k]
            if cum not in table:
                table[cum]=1
            else:
                table[cum]+=1
        return count
```
