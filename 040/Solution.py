class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates=sorted(candidates)
        res=[]
        path=[]
        self.dfs(candidates,0,res,target,path,[])
        return res
        
    
    def dfs(self,nums,index,res,target,path,visited):
        if target<0:
            return
        if target==0 and path not in res:
            res.append(path)
            return
        else:
            for i in range(index,len(nums)):
                if nums[i]>target:
                    return
                if i not in visited:
                    self.dfs(nums,i,res,target-nums[i],path+[nums[i]],visited+[i])