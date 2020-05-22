class Solution:
    def jump(self, nums: List[int]) -> int:
        cur=0
        pos=0
        count=0
        pre=0
        while cur<len(nums)-1:
            count+=1
            pre=cur
            while pos<=pre:
                cur=max(cur,pos+nums[pos])
                pos+=1
        return count