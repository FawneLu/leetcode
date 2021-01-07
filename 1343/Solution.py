class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0]
        res = 0
        for i in arr:
            prefix_sum.append(prefix_sum[-1] + i)
        for i in range(len(arr) - k + 1):
            if prefix_sum[i+k] - prefix_sum[i] >= threshold * k:
                res += 1
        return res
        
        
        
        
    def numOfSubarrays1(self, arr: List[int], k: int, threshold: int) -> int:
        if threshold > sum(arr) or k > len(arr):
            return 0
        
        res, target, low, cur_sum  = 0, threshold * k, -1, 0
        
        for high, value in enumerate(arr):
            cur_sum += value
            
            if high - low == k:
                if cur_sum >= target:
                    res += 1
                low += 1    
                cur_sum -= arr[low]
       
        
        return res