class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left , right = 0 , len(arr)-1
        while left < right-1:
            mid = left + (right - left)//2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        
       
        res , count = [] , 0
        while left >= 0 and right <= len(arr)-1 and count < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left-=1
                count+=1
            else:
                res.append(arr[right])
                right+=1
                count+=1
        
        
        if count < k:
            if left < 0 :
                while count < k:
                    res.append(arr[right])
                    right+=1
                    count+=1
            else:
                while count < k:
                    res.append(arr[left])
                    left-=1
                    count+=1
        
        return sorted(res)