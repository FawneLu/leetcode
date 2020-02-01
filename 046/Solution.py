```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        visited=[0]*len(nums)
        
        def backtracking(path):
            if len(path)==len(nums):
                res.append(path)
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=1
                    backtracking(path+[nums[i]])
                    visited[i]=0
        
        backtracking(path)
        return res
```
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]
        path=[]
        res=[]
        self.dfs(nums,path,res)
        return res
        
    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]],res)
```