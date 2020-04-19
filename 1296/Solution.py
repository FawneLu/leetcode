class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count=collections.Counter(nums)
        nums = deque(sorted(list(set(nums))))
        while nums:
            num=nums[0]
            for j in range(k):
                if num+j not in count or count[num+j]==0:
                    return False
                else:
                    count[num+j]-=1
                if count[num+j]==0:
                    nums.popleft()
        
        return True