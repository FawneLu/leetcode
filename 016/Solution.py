class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                cum=nums[i]+nums[left]+nums[right]
                if abs(target-cum)<abs(target-res):
                    res=cum
                
                if cum>target:
                    right-=1
                elif cum<target:
                    left+=1
                else:
                    return cum
        
        return res