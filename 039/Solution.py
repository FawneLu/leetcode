```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = [0]*len(candidates)
        res=[]
        def dfs(solutions, level, leftmoney):
            if level == len(candidates)-1:
                if leftmoney % candidates[level] == 0:
                    solutions[level] = leftmoney//candidates[level]
                    ans=[]
                    tmp = []
                    for i in range(len(candidates)):
                        tmp += [candidates[i]]*solutions[i]
                    res.append(tmp)
                return

            for i in range(leftmoney//candidates[level] + 1):
                solutions[level] = i
                dfs(solutions, level+1, leftmoney - i*candidates[level] )
        
        dfs(solutions, 0, target)
        return res


    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates=sorted(candidates)
        res=[]
        path=[]
        self.dfs(candidates,0,res,target,path)
        return res
        
    
    def dfs(self,nums,index,res,target,path):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        else:
            for i in range(index,len(nums)):
                if nums[i]>target:
                    return
                self.dfs(nums,i,res,target-nums[i],path+[nums[i]])
```