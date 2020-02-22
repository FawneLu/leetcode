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
- 二分查找  
这道题还可以用一个二分查找  
target = sums[i]-s, 找第一个大于等于target的pos。  
如果sums[i]-sums[pos]==s, return i-pos  
如果sums[i]-sums[pos]< s, return i-pos+1  
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        def binary_search(nums,target):
            left=0
            right=len(nums)
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]>=target:
                    if mid==0 or nums[mid-1]<target:
                        return mid
                    else: right=mid-1
                else:
                    left=mid+1
            
            return left
                    
        pre_sum=[]
        pre_sum.append(0)
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        
        res=float('inf')
        for i in range(len(pre_sum)):
            target=pre_sum[i]-s
            if target<0:
                continue
            pos=binary_search(pre_sum,target)
            
            if pre_sum[i]-pre_sum[pos]==s:
                res=min(res,i-pos)
            if pre_sum[i]-pre_sum[pos]<s:
                res=min(res,i-pos+1)
        
        return 0 if res==float('inf') else res
```