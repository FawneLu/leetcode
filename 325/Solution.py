class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        cum = 0
        cur_sum = {}
        for i in range(len(nums)):
            cum += nums[i]
            if cum == k:
                res = i+1
            elif cum-k in cur_sum:
                res = max(res, i - cur_sum[cum - k])
            if cum not in cur_sum:
                cur_sum[cum] = i
        return res