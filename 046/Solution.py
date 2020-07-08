class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(index, layer):
            if layer == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index+1, layer+1)
                nums[i], nums[index] = nums[index], nums[i]
        
        dfs(0,0)
        return res
        
        
    
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited=[0] * len(nums)
            
        def dfs(layer, solutions):
            if layer == len(nums):
                res.append(solutions)
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    dfs(layer+1, solutions+[nums[i]])
                    visited[i] = 0
            
        dfs(0, [])
        return res

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