class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(mid):
            i,count = 0,0
            for j in range(len(nums)):
                while nums[j] - nums[i] > mid:
                    i+=1
                count += j-i
            return count
            
        
        nums.sort()
        left, right = 0 , nums[-1]-nums[0]
        while left <= right:
            mid = left + (right-left)//2
            if helper(mid) < k:
                left = mid+1
            else:
                right = mid-1
        return left