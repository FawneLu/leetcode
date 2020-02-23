```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:
            return False
        target=sum(nums)/k
        visited=[0]*len(nums)
        
        def dfs(index,k,count,cum):
            if k==1:
                return True
            if cum==target and count>0:
                return dfs(0,k-1,0,0)
            for i in range(index,len(nums)):
                if not visited[i] and cum+nums[i]<=target:
                    visited[i]=1
                    if dfs(i+1,k,count+1,cum+nums[i]):
                        return True
                    visited[i]=0
            return False
        
        return dfs(0,k,0,0)
```