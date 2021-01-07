class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        end, res = 0 , 0
        
        while end < len(arr):
            base = end
            while end < len(arr)-1 and arr[end] < arr[end+1]:
                end +=1 
            
            if end == base:
                end += 1
                continue
            
            peak = end
            
            while end < len(arr)-1 and arr[end] > arr[end+1]:
                end +=1 
            
            if end == peak:
                end += 1
                continue
            
            res = max(res, end - base + 1)
        
        return res