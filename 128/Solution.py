```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        d={}
        n=len(nums)
        for num in nums:
            if num not in d:
                left=d.get(num-1,0)
                right=d.get(num+1,0)
                
                length=left+right+1
                res=max(res,length)
                
                d[num]=length
                d[num-left]=length
                d[num+right]=length
        
        return res
```