```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        res=[]
        for i,val in enumerate(nums):
            if i>=k and i-stack[0]>=k:
                stack.pop(0)
            while stack and nums[stack[-1]]<val:
                stack.pop()
            
            stack.append(i)
            if i>k-2:
                res.append(nums[stack[0]])
        
        return res
```
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n*k==0:
            return []
        if k==1:
            return nums
        
        res=[]
        
        queue=collections.deque()
        for i in range(k-1):
            while queue:
                if len(queue) and nums[queue[-1]]<=nums[i]:
                    queue.pop()
                else:
                    break
            queue.append(i)
            
        
        for i in range(k-1,n):
            while queue:
                if len(queue) and nums[queue[-1]]<=nums[i]:
                    queue.pop()
                else:
                    break
            queue.append(i)
            
            while queue and queue[0]<i-k+1:
                queue.popleft()
            
            res.append(nums[queue[0]])
        
        return res
```