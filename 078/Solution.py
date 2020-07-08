```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])
        res = []
        dfs(0, [])
        return res
```
```python
class Solution:  
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res
```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(layer, solutions):
            if layer == len(nums):
                res.append(solutions)
                return 
            
            dfs(layer+1, solutions+[nums[layer]])
            dfs(layer+1, solutions)
            
        dfs(0, [])
        return res