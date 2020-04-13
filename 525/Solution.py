class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        index=dict()
        index[0]=-1
        total=0
        for i,num in enumerate(nums):
            if num==0:
                total-=1
            else:
                total+=1
            
            if total in index:
                res=max(res,i-index[total])
            else:
                index[total]=i
        
        return res