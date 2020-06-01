class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        visited=[0]*len(nums)
        
        def backtracking(path):
            if len(path)==len(nums) and path not in res:
                res.append(path)
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=1
                    backtracking(path+[nums[i]])
                    visited[i]=0
        
        backtracking(path)
        return res