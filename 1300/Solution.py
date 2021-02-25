class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if target == sum(arr):
            return max(arr)
        
        n = len(arr)
        left, right = 0 , max(arr)
        
        res, sub = float("inf"), float("inf")
        
        while left <= right:
            mid = (right - left)//2 + left
            cum = 0
            for num in arr:
                if num > mid :
                    cum += mid
                else:
                    cum += num
            
            cur_sub = abs(cum-target)
            if cur_sub < sub:
                res = mid
                sub = cur_sub
            elif cur_sub == sub:
                res = min(res,mid)
            
            
            if cum > target:
                right = mid - 1
            
            if cum < target:
                left = mid + 1
            
            if cum == target:
                return mid
        
        return res